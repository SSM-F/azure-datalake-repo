from azure.storage.filedatalake import DataLakeServiceClient
from src.credentials import get_service_token_credential

def test_connect_azure_data_lake():
    account_name = "firstlakessmf"
    client = get_service_token_credential(account_name)
    file_system = list(client.list_file_systems())
    
    assert isinstance(client,DataLakeServiceClient)
    assert len(file_system) > 0