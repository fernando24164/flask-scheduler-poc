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

    async def put_item(self, table_name):
        with self.dynamo as dynamo_resource:
            response = await dynamo_resource.put_item(table_name)

        return response

    async def get_item(self, table_name):
        with self.dynamo as dynamo_resource:
            response = await dynamo_resource.get_item(table_name)

        return response

    async def update_item(self, table_name):
        with self.dynamo as dynamo_resource:
            response = await dynamo_resource.update_item(table_name)

        return response
