from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import AzureError
import logging

def get_list_of_files(connection_string,file_system_name,directory_path):
    try:
        service_client = DataLakeServiceClient.from_connection_string(conn_str=connection_string)
        file_client = service_client.get_file_system_client(file_system=file_system_name)
        result = []
        path_client = file_client.get_paths(path=directory_path, recursive=True)
        for path in path_client:
            result.append(path)
            logging.info(f"Succesfully extracted files info")


        return result
    except AzureError:
        logging.error("Failed request, please check that values passed are correct")