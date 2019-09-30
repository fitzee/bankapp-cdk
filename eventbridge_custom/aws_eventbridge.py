from aws_cdk import (aws_lambda as lambda_, aws_cloudformation as cfn, aws_iam as iam, core)
from typing import (Optional, Mapping, List)


class event_bus(core.Construct):
    def __init__(self, scope: core.Construct, id: str, name: str, rules: Optional[List[Mapping[str, str]]] = None,
                 targets: Optional[List[Mapping[str, str]]] = None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        custom_role = iam.Role(self, 'EventBridgeCustomRole', assumed_by=iam.ServicePrincipal('lambda'),
                               managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name('AmazonEventBridgeFullAccess'),
                                                 iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchLogsFullAccess')])

        resource = cfn.CustomResource(self, 'Resource', provider=cfn.CustomResourceProvider.lambda_(
            lambda_.SingletonFunction(self, 'Singleton', uuid='2bdf7084-233d-42c1-8e33-1dc6bd2716ca',
                                      timeout=core.Duration.seconds(300),
                                      role=custom_role,
                                      handler='eventbridge-handler.main',
                                      code=lambda_.Code.from_asset('eventbridge_custom/eventbridge_handler'),
                                      runtime=lambda_.Runtime.PYTHON_3_7)),
                                      properties={'name': name, 'rules': rules, 'targets': targets})

        self._response = resource.get_att('EventBusArn').to_string()

    @property
    def response(self):
        return self._response
