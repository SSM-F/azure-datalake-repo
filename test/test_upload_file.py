from src.upload_file import upload_file

from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import ClientAuthenticationError
from unittest.mock import patch,MagicMock
from dotenv import load_dotenv

load_dotenv(dotenv_path='example.env') 
import os
import logging
import pytest


def test_upload_file():
    file_system_name = 'myfirstcontainer'
    file_path = 'data/customer_industries.json'
    connection_string = os.getenv("CONNSTRING")
   
    
    response = upload_file(connection_string,
                           file_system_name,
                           file_path,
                           )
    assert isinstance(response,DataLakeServiceClient)

def test_upload_file_logs_succesful_message(caplog):
    file_system_name = 'myfirstcontainer'
    file_path = 'data/customer_industries.json'
    connection_string = os.getenv("CONNSTRING")

    with caplog.at_level(logging.INFO):
        upload_file(connection_string,
                           file_system_name,
                           file_path,
                           )
    assert "File uploaeded succesfully" in caplog.text

@patch('src.upload_file.DataLakeServiceClient.from_connection_string')
def test_upload_file_ClientAuthenticationError(mock_con_string,caplog):
    mock_con_string.side_effect = ClientAuthenticationError()
    
    with caplog.at_level(logging.CRITICAL):
        response = upload_file('test',
                           'test',
                           'test',
                           )
    assert "Was not able to connect to account, please check connection string syntax" in caplog.text
    assert response == "Error uploading the file"




