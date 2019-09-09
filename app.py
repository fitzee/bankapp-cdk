#!/usr/bin/env python3

from aws_cdk import core

from bankapp_cdk.bankapp_cdk_stack import BankappCdkStack


app = core.App()
BankappCdkStack(app, "bankapp-cdk")

app.synth()
