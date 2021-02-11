from aws_cdk import (
    aws_s3 as s3,
    core,
    aws_dynamodb,
    aws_lambda,
    aws_apigateway as apigateway,

)


class DemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.table_name = 'globaldatatest.global.table'
        executelambda = aws_lambda.Function(self, id='execute', runtime=aws_lambda.Runtime.PYTHON_3_8,
                                            handler='execute.lambda_handler', code=aws_lambda.Code.asset('lambda'))

        statsLambda = aws_lambda.Function(self, id='stats', runtime=aws_lambda.Runtime.PYTHON_3_8,
                                          handler='stats.lambda_handler', code=aws_lambda.Code.asset('lambda'))

        resetLambda = aws_lambda.Function(self, id='reset', runtime=aws_lambda.Runtime.PYTHON_3_8,
                                          handler='reset.lambda_handler', code=aws_lambda.Code.asset('lambda'))

        my_bucket = s3.Bucket(self, id='s3buckset3', bucket_name='s3mybucket')
        table = aws_dynamodb.Table(
            self,
            'table3',
            partition_key={'name': 'key', 'type': aws_dynamodb.AttributeType.STRING},
            table_name='commands')
        api = apigateway.RestApi(self, "web-shell-apii", rest_api_name="Web Shell",
                                 description="This service serves shell commands.")
        executeIntegration = apigateway.LambdaIntegration(executelambda)
        statsIntegration = apigateway.LambdaIntegration(statsLambda)
        resetIntegration = apigateway.LambdaIntegration(resetLambda)

        executeResource = api.root.add_resource('execute')
        executeResource.add_method("POST", executeIntegration, api_key_required=True)

        statsResource = api.root.add_resource('stats')
        statsResource.add_method("GET", statsIntegration, api_key_required=True)

        resetResource = api.root.add_resource('reset')
        resetResource.add_method("PUT", resetIntegration, api_key_required=True)
