from aws_cdk import (
    # Duration,
    CfnOutput,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as _s3,
    aws_iam as _iam
)
from constructs import Construct

class CourseRepoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CourseRepoQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        _s3.Bucket(
            self,
            "mybucketid",
            bucket_name="coursebucket1414",
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "mybucketid1"
        )

        _iam.Group(
            self,
            "gid"
        )

        output_1 = CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description="first cdk bucket",
            export_name="myBucketOutput1"
        )
