from azure.storage.filedatalake import FileSystemClient, DataLakeServiceClient

def create_file_system(service_client: DataLakeServiceClient, file_system_name: str)-> FileSystemClient:
    file_system_client = service_client.create_file_system(file_system=file_system_name)
    return file_system_client