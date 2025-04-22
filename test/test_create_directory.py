from azure.storage.filedatalake import FileSystemClient, DataLakeDirectoryClient

from src.create_directory import create_directory
from unittest.mock import MagicMock,patch

def test_create_directory():
    
    mock_fs_client = MagicMock(spec=FileSystemClient)
    mock_directory_client = MagicMock(spec= DataLakeDirectoryClient)
    mock_fs_client.create_directory.return_value = mock_directory_client
    directory_name = 'testdirectory'
    response = create_directory(mock_fs_client,directory_name)
   
    assert isinstance(response,DataLakeDirectoryClient)

   