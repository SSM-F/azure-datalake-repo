import os
from azure.storage.filedatalake import (
    DataLakeServiceClient,
    DataLakeDirectoryClient,
    FileSystemClient,
    DataLakeFileClient
)
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureNamedKeyCredential
import json
from dotenv import load_dotenv
from azure.core.exceptions import ClientAuthenticationError
import pandas as pd

load_dotenv(dotenv_path='example.env') 



def upload_file(connection_string,
                           file_system_name,
                           file_path,
                           ):
    
    try:
        service_client = DataLakeServiceClient.from_connection_string(conn_str=connection_string)
        file_client = service_client.get_file_client(file_system= file_system_name, file_path=file_path)
        try:
            file_client.create_file()
        except Exception:
            raise Exception("File already exists")

        with open(file_path, 'r') as file:
            
            data_json = json.load(file)
            dta_frame = pd.DataFrame(data_json)
            
        data=dta_frame.to_json(orient="records")
        file_client.append_data(data=data,offset=0,length=len(data))
        
        file_client.flush_data(len(data))
        

        return "File uploaded succesfully"

    except ClientAuthenticationError:
        return "Error uploading the file"