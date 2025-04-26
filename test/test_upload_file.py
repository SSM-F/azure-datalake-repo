from src.upload_file import upload_file

from azure.storage.filedatalake import DataLakeServiceClient

from dotenv import load_dotenv

load_dotenv(dotenv_path='example.env') 
import os
import logging



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





    #file_path_2 = 'data/vehicle_customers.json'
    #response_2 = upload_file(connection_string,
    #                       file_system_name,
    #                       file_path_2,
    #                       )



