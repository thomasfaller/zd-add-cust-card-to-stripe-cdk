#!/usr/bin/env python3

from aws_cdk import core

from zd_add_cust_card_to_stripe_cdk.zd_add_cust_card_to_stripe_cdk_stack import ZdAddCustCardToStripeCdkStack


app = core.App()
ZdAddCustCardToStripeCdkStack(app, "zd-add-cust-card-to-stripe-cdk")

app.synth()
