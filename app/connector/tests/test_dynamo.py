import pytest
from unittest import TestCase
from moto import mock_dynamodb2
from ..dynamo_connector import DynamoConnector


class TestDynamo(TestCase):
    """
    Class to test async
    """

    @mock_dynamodb2
    def setUp(self):
        self.connector = DynamoConnector()

    @mock_dynamodb2
    def tearDown(self):
        del self.connector

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_create_table(self):
        response = self.connector.create_table('test')
        self.assertIsNotNone(response)

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_update_item(self):
        self.connector.put_item('test',{
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    })

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_get_item(self):
        self.connector.get_item('test', {
        'username': 'janedoe',
        'last_name': 'Doe'
    })

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_update_item(self):
        self.connector.update_item('test', {
            'username': 'janedoe',
            'last_name': 'Doe'
        },
                                   'SET age = :val1',
                                   {
                                       ':val1': 26
                                   })
