from aws_cdk import (aws_iam as iam, aws_lambda as lambda_ , aws_events as events,
                     aws_events_targets as targets, core)

from typing import Optional


class EventBridgeCreatorStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,  bank_account_service: lambda_.Function,
                 stage: Optional[str] = 'prod', **kwargs) -> None:
        super().__init__(scope, id+'-'+stage, **kwargs)

        bus_name = 'banking-demo-events-'+stage
        bus = events.EventBus(self, id, event_bus_name=bus_name)
        events.Rule(self, "APPLICATION_SUBMITTED", event_bus=bus, event_pattern=events.EventPattern(
            detail_type=["APPLICATION_SUBMITTED"]), rule_name="APPLICATION_SUBMITTED", enabled=True)
        events.Rule(self, "APPLICATION_APPROVED", event_bus=bus, event_pattern=events.EventPattern(
            detail_type=["APPLICATION_APPROVED"]), rule_name="APPLICATION_APPROVED", enabled=True,
                         targets=[
                             targets.LambdaFunction(lambda_.Function.from_function_arn(
                                 self, "func", bank_account_service.function_arn))
                         ])

        self._event_bus_arn = bus.event_bus_arn

    @property
    def event_bus_arn(self):
        return self._event_bus_arn
