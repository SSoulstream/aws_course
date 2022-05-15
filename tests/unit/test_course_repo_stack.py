import aws_cdk as core
import aws_cdk.assertions as assertions

from course_repo.course_repo_stack import CourseRepoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in course_repo/course_repo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CourseRepoStack(app, "course-repo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
