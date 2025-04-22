
from azure.storage.filedatalake import FileSystemClient, DataLakeDirectoryClient

def create_directory(file_system_client: FileSystemClient,directory_name:str) -> DataLakeDirectoryClient:
    directory_client = file_system_client.create_directory(directory_name)
    
    return directory_client
        