from aws_cdk import (aws_dynamodb as ddb, aws_stepfunctions as sf, aws_stepfunctions_tasks as sft, aws_ssm as ssm,
                     aws_lambda as lambda_, aws_lambda_event_sources as lambda_es, aws_apigateway as gw,
                     aws_iam as iam, core)
from typing import Optional


class AccountApplicationServiceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, id_checker: str, event_bus: str, stage: Optional[str] = 'prod',
                 **kwargs) -> None:
        super().__init__(scope, id+'-'+stage, **kwargs)

        app_table_name = id + '-applications-table-' + stage
        app_table = ddb.Table(self, id=app_table_name, table_name=app_table_name,
                              partition_key=ddb.Attribute(name='id', type=ddb.AttributeType.STRING),
                              billing_mode=ddb.BillingMode.PAY_PER_REQUEST)

        events_table_name = id + '-events-table-' + stage
        events_table = ddb.Table(self, id=events_table_name, table_name=events_table_name,
                                 partition_key=ddb.Attribute(name='id', type=ddb.AttributeType.STRING),
                                 billing_mode=ddb.BillingMode.PAY_PER_REQUEST, stream=ddb.StreamViewType.NEW_IMAGE)

        self._table_stream_arn = events_table.table_stream_arn

        # create our Lambda function for the bank account service
        func_name = id + '-' + stage + '-' + 'account-application'
        lambda_assets = lambda_.Code.from_asset('account_application_service')
        handler = lambda_.Function(self, func_name, code=lambda_assets,
                                   runtime=lambda_.Runtime.NODEJS_10_X, handler='main.handler',
                                   environment={'ACCOUNTS_TABLE_NAME': app_table.table_name,
                                                'EVENTS_TABLE_NAME': events_table.table_name,
                                                'REGION': core.Aws.REGION})

        gw.LambdaRestApi(self, id=stage + '-' + id, handler=handler)

        # grant main Lambda function access to DynamoDB tables
        app_table.grant_read_write_data(handler.role)
        events_table.grant_read_write_data(handler.role)

        p_statement = iam.PolicyStatement(actions=['ssm:Describe*', 'ssm:Get*', 'ssm:List*', 'events:*', 'states:*'],
                                          effect=iam.Effect.ALLOW, resources=['*'])
        handler.add_to_role_policy(statement=p_statement)

        # create the Lambda function for the event publisher
        evt_publisher = id + '-' + stage + '-' + 'event-publisher'
        evt_handler = lambda_.Function(self, evt_publisher, code=lambda_assets,
                                       runtime=lambda_.Runtime.NODEJS_10_X, handler='event-publisher.handler',
                                       events=[lambda_es.DynamoEventSource(table=events_table,
                                                                           starting_position=lambda_.StartingPosition.LATEST)],
                                       environment={'EVENT_BRIDGE_ARN': event_bus,
                                                    'REGION': core.Aws.REGION}
                                       )

        evt_handler.add_to_role_policy(statement=p_statement)

        # set up StepFunctions
        approve_application = sf.Task(self, 'Approve Application',
                                      task=sft.InvokeFunction(handler, payload={
                                          'body': {
                                              'command': 'APPROVE_ACCOUNT_APPLICATION',
                                              'data': {'id.$': '$.application.id'}
                                          }
                                      }), result_path='$.approveApplication')

        reject_application = sf.Task(self, 'Reject Application',
                                     task=sft.InvokeFunction(handler, payload={
                                         'body': {
                                             'command': 'REJECT_ACCOUNT_APPLICATION',
                                             'data': {
                                                 'id.$': '$.application.id'
                                             }
                                         }
                                     }), result_path='$.rejectApplication')

        id_checker_handler = lambda_.Function.from_function_arn(self, 'IdentityChecker', function_arn=id_checker)
        check_identity = sf.Task(self, 'Check Identity',
                                 task=sft.InvokeFunction(id_checker_handler, payload={
                                     'body': {
                                         'command': 'CHECK_IDENTITY',
                                         'data': {'application.$': '$.application'}
                                     }
                                 }))

        wait_for_human_review = sf.Task(self, 'Wait for Human Review',
                                        task=sft.RunLambdaTask(handler,
                                                               integration_pattern=sf.ServiceIntegrationPattern.WAIT_FOR_TASK_TOKEN,
                                                               payload={
                                                                   'body': {
                                                                       'command': 'FLAG_ACCOUNT_APPLICATION_FOR_HUMAN_REVIEW',
                                                                       'data': {
                                                                           'id.$': '$.application.id',
                                                                           'taskToken': sf.Context.task_token
                                                                       }
                                                                   }
                                                               }), result_path='$.humanReview') \
            .next(
            sf.Choice(self, 'Human Approval Choice')
            .when(sf.Condition.string_equals('$.humanReview.decision', 'APPROVE'), next=approve_application)
            .when(sf.Condition.string_equals('$.humanReview.decision', 'REJECT'), next=reject_application))

        sm_definition = sf.Parallel(self, 'Perform Automated Checks', result_path='$.checks') \
            .branch(check_identity) \
            .branch(sf.Pass(self, 'Check Fraud Model', result=sf.Result({'flagged': False}))) \
            .next(
            sf.Choice(self, 'Automated Checks Choice')
                .when(sf.Condition.boolean_equals('$.checks[0].flagged', True), next=wait_for_human_review)
                .when(sf.Condition.boolean_equals('$.checks[1].flagged', True), next=wait_for_human_review)
                .otherwise(approve_application))

        state_machine = sf.StateMachine(self, 'OpenAccountStateMachine'+stage, definition=sm_definition)
        ssm.CfnParameter(self, id='StateMachineArnSSM', type='String', value=state_machine.state_machine_arn,
                         name='StateMachineArnSSM')

    @property
    def table_stream_arn(self):
        return self._table_stream_arn
