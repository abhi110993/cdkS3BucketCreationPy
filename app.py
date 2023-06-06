#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_s3app.cdk_s3app_stack import CdkS3AppStack

app = cdk.App()
CdkS3AppStack(app, "CdkS3AppStack",
              env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                                  region=os.getenv('CDK_DEFAULT_REGION'))
              )
app.synth()
