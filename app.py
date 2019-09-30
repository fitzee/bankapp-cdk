from aws_cdk import core

from bankapp_cdk.bank_account_service import BankAccountServiceStack
from bankapp_cdk.eventbridge_creator import EventBridgeCreatorStack
from bankapp_cdk.account_application_service import AccountApplicationServiceStack
from bankapp_cdk.identity_checking_service import IdentityCheckingServiceStack

stage = 'dev'

app = core.App()
bas = BankAccountServiceStack(app, "BankAccountService", stage=stage)
eb = EventBridgeCreatorStack(app, "EventBridgeCreator", bank_account_service=bas.bank_account_service, stage=stage)
ics = IdentityCheckingServiceStack(app, "IdentityCheckingService", stage=stage)
AccountApplicationServiceStack(app, "AccountApplicationService", id_checker=ics.identity_checking_service_arn,
                               event_bus=eb.event_bus_arn, stage=stage)

app.synth()
