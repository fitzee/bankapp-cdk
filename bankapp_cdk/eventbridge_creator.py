from aws_cdk import (aws_iam as iam, aws_lambda as lambda_ , core)
from eventbridge_custom import aws_eventbridge as eb
from typing import Optional


class EventBridgeCreatorStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,  bank_account_service: lambda_.Function,
                 stage: Optional[str] = 'prod', **kwargs) -> None:
        super().__init__(scope, id+'-'+stage, **kwargs)

        bus_name = 'banking-demo-events-'+stage
        bus = eb.event_bus(self, 'eventbridge', name=bus_name,
                           rules=[{'name': 'APPLICATION_SUBMITTED',
                                   'state': 'ENABLED',
                                   'pattern': '{ "detail-type": ["APPLICATION_SUBMITTED"] }'
                                   },
                                  {'name': 'APPLICATION_APPROVED',
                                   'state': 'ENABLED',
                                   'pattern': '{ "detail-type": ["APPLICATION_APPROVED"] }'
                                   }
                                  ],
                           targets=[{'rule': 'APPLICATION_APPROVED',
                                    'arns': [bank_account_service.function_arn]}])

        self._event_bus_arn = bus.response

    @property
    def event_bus_arn(self):
        return self._event_bus_arn
