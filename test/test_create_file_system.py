from create_file_system import create_file_system
from azure.storage.filedatalake import FileSystemClient, DataLakeServiceClient
from src.credentials import get_service_token_credential
from unittest.mock import MagicMock, patch


def test_create_file_system():
    file_system_name = 'testfilesystem123233212'
    account_name = "firstlakessmf"

    service_client = get_service_token_credential(account_name)
    mock_fs_client = MagicMock(spec=FileSystemClient)
    mock_fs_client.file_system_name = file_system_name
    
    with patch.object(service_client, "create_file_system", return_value = mock_fs_client) as mock_cred:

        response = create_file_system(service_client=service_client,file_system_name=file_system_name)
  
        assert isinstance(response,FileSystemClient)
        assert response.file_system_name == file_system_name
    