import azure.functions as func
from src.func_app import main

def test_succesfull_request():
    test_req = func.HttpRequest(
        method='GET',
        url='/api/azure-data-lake-gen2',
        params={'name':'Alice'},
        body=None
    )
    response = main(test_req)
    assert response.status_code == 200
    assert response.get_body().decode() == 'Hello there, Alice!'

def test_no_name_request():
    test_req= func.HttpRequest(
        method="GET",
        url="api/azure-data-lake-gen2",
        params={'name':None},
        body=None
    )
    response = main(test_req)
    assert response.status_code == 400
    assert response.get_body().decode() == "Please pass a name, dont be rude"