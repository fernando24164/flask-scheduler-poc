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

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_create_table(self):
        self.connector.create_table('test')

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_update_item(self):
        self.connector.put_item('test')

    @pytest.mark.asyncio
    @mock_dynamodb2
    def test_get_item(self):
        self.connector.get_item('test')
