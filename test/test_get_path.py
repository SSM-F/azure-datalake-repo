from azure.storage.filedatalake import DataLakeServiceClient
from src.get_path import get_list_of_files
from dotenv import load_dotenv
import os
import logging
from unittest.mock import MagicMock,patch
from azure.core.exceptions import AzureError
load_dotenv(dotenv_path='example.env') 


def test_get_list_of_files():
    connection_string = os.getenv("CONNSTRING")
    file_system_name = 'myfirstcontainer'
    directory_path = 'data'
    response = get_list_of_files(connection_string,file_system_name,directory_path)
    assert isinstance(response,list)
    assert response[0]['name'] == 'data/customer_industries.json'
    assert response[1]['name'] == 'data/vehicle_customers.json'


def test_succesful_log(caplog):
    connection_string = os.getenv("CONNSTRING")
    file_system_name = 'myfirstcontainer'
    directory_path = 'data'

    with caplog.at_level(logging.INFO):
        get_list_of_files(connection_string,file_system_name,directory_path)
    assert "Succesfully extracted files info" in caplog.text

@patch("src.get_path.DataLakeServiceClient.from_connection_string")
def test_RequestFailedException_get_list_of_files(mock_con_str,caplog):
    mock_con_str.side_effect = AzureError(message="Failed request")

    with caplog.at_level(logging.ERROR):
        response = get_list_of_files('test','test','test')

    assert "Failed request, please check that values passed are correct" in caplog.text
