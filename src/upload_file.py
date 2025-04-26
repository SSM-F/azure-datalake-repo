
from azure.storage.filedatalake import DataLakeServiceClient
import json
from azure.core.exceptions import ClientAuthenticationError
import pandas as pd
import logging



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
        
        logging.info("File uploaeded succesfully")
        return service_client

    except ClientAuthenticationError:
        logging.critical("Was not able to connect to account, please check connection string syntax")
        return "Error uploading the file"