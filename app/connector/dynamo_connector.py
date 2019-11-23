import aioboto3


class DynamoConnector:
    """
    Class to connect to to DynamoDB
    """
    def __init__(self):
        self.dynamo = aioboto3.resource('dynamodb', 'us-east-1')

    async def create_table(self, table_name):
        """
        Method to create a table in dynamoDB
        :param table_name:
        :return:
        """
        with self.dynamo as dynamo_resource:
            response = await dynamo_resource.create_table(table_name)

        return response

    async def put_item(self, table_name, item):
        with self.dynamo as dynamo_resource:
            table = dynamo_resource.Table(table_name)
            response = await table.put_item(Item=item)

        return response

    async def get_item(self, table_name, key):
        with self.dynamo as dynamo_resource:
            table = dynamo_resource.Table(table_name)
            response = await table.get_item(Key=key)

        return response['Item']

    async def update_item(self, table_name, key, updateExpression,
                          expressionAttributeValues):
        with self.dynamo as dynamo_resource:
            table = dynamo_resource.Table(table_name)
            response = await table.update_item(
                Key=key,
                UpdateExpression=updateExpression,
                ExpressionAttributeValues=expressionAttributeValues)

        return response
