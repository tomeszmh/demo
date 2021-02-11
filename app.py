#!/usr/bin/env python3

from aws_cdk import core

from demo.demo_stack import DemoStack
import os

app = core.App()
DemoStack(app, "demoProject")

app.synth()
