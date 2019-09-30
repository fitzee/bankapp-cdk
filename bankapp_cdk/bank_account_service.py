from aws_cdk import (aws_dynamodb as ddb, aws_lambda as lambda_, aws_apigateway as gw, aws_iam as iam, core)
from typing import Optional


class BankAccountServiceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, stage: Optional[str] = 'prod', **kwargs) -> None:
        super().__init__(scope, id+'-'+stage, **kwargs)

        acct_table_name = id+'-accounts-table-'+stage
        acct_table = ddb.Table(self, id=acct_table_name, table_name=acct_table_name,
                               partition_key=ddb.Attribute(name='id', type=ddb.AttributeType.STRING),
                               billing_mode=ddb.BillingMode.PAY_PER_REQUEST)

        events_table_name = id+'-events-table-'+stage
        events_table = ddb.Table(self, id=events_table_name, table_name=events_table_name,
                                 partition_key=ddb.Attribute(name='id', type=ddb.AttributeType.STRING),
                                 billing_mode=ddb.BillingMode.PAY_PER_REQUEST, stream=ddb.StreamViewType.NEW_IMAGE)

        self._table_stream_arn = events_table.table_stream_arn

        # create our Lambda function for the bank account service
        func_name = id+'-'+stage+'-'+'bank-accounts'
        handler = lambda_.Function(self, func_name, code=lambda_.Code.from_asset('bank_account_service'),
                                   runtime=lambda_.Runtime.NODEJS_10_X, handler='handler.handler',
                                   environment={'ACCOUNTS_TABLE_NAME': acct_table.table_name,
                                                'EVENTS_TABLE_NAME': events_table.table_name,
                                                'REGION': core.Aws.REGION})

        self._bank_account_service = handler

        gw.LambdaRestApi(self, id=stage+'-'+id, handler=handler)

        # give EventBridge permission to invoke this Lambda
        handler.add_permission(id='EBPermission', principal=iam.ServicePrincipal('events.amazonaws.com'),
                               action='lambda:InvokeFunction')

        acct_table.grant_read_write_data(handler.role)
        events_table.grant_read_write_data(handler.role)

    @property
    def table_stream_arn(self):
        return self._table_stream_arn

    @property
    def bank_account_service(self):
        return self._bank_account_service
