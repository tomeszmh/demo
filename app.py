#!/usr/bin/env python3

from aws_cdk import core

from demo.demo_stack import DemoStack


app = core.App()
DemoStack(app, "demo")

app.synth()
