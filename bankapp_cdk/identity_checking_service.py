from aws_cdk import (aws_ssm as ssm, aws_lambda as lambda_, core)
from typing import Optional


class IdentityCheckingServiceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, stage: Optional[str] = 'prod', **kwargs) -> None:
        super().__init__(scope, id+'-'+stage, **kwargs)

        func_name = id + '-' + stage
        handler = lambda_.Function(self, func_name, code=lambda_.Code.from_asset('identity_checking_service'),
                                   runtime=lambda_.Runtime.NODEJS_10_X, handler='main.handler')

        ssm.CfnParameter(self, id='ServiceEndpointSSM', name='ServiceEndpointSSM',
                         type='String', value=handler.function_arn)
        self._identity_checking_service_arn = handler.function_arn

    @property
    def identity_checking_service_arn(self):
        return self._identity_checking_service_arn
