from src.upload_file import upload_file
from src.credentials import get_service_token_credential
from src.create_directory import create_directory

from azure.storage.filedatalake import DataLakeDirectoryClient
from unittest.mock import MagicMock,patch
from mocks import *
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path='example.env') 
import os



def test_upload_file():

    file_system_name = 'myfirstcontainer'
    file_path = 'data/customer_industries.json'
    #account_name = os.getenv('ACCOUNTNAME')
    #account_key= os.getenv('ACCOUNTKEY')
    connection_string = os.getenv("CONNSTRING")
   
    
    response = upload_file(connection_string,
                           file_system_name,
                           file_path,
                           )
    assert response == "File uploaded succesfully"


