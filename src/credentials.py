
import os

from azure.storage.filedatalake import DataLakeServiceClient
from azure.identity import DefaultAzureCredential


def get_service_token_credential(account_name) -> DataLakeServiceClient:
    account_url = f"https://{account_name}.dfs.core.windows.net"
    token_credential = DefaultAzureCredential()
    service_client = DataLakeServiceClient(account_url,credential=token_credential)

    return service_client