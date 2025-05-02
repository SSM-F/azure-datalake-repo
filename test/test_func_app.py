import azure.functions as func
from src.func_app import main,post
import json

class TestGET:
    def test_succesfull_request(self):
        test_req = func.HttpRequest(
            method='GET',
            url='/api/azure-data-lake-gen2',
            params={'name':'Alice'},
            body=None
        )
        response = main(test_req)
        assert response.status_code == 200
        assert response.get_body().decode() == 'Hello there, Alice!'

    def test_no_name_request(self):
        test_req= func.HttpRequest(
            method="GET",
            url="/api/azure-data-lake-gen2",
            params={'name':None},
            body=None
        )
        response = main(test_req)
        assert response.status_code == 400
        assert response.get_body().decode() == "Please pass a name, dont be rude"

class TestPOST:
    def test_succesfull_post(self):
        test_post_body={'name':'Mario',
                        'surname':'SuperStar'}
        request= func.HttpRequest(
            method='POST',
            url='/api/azure-data-lake-gen2',
            body=json.dumps(test_post_body).encode('utf-8'),
            headers={
                'Content-Type':'application/json'
            }
        )
        response= post(request)
        assert response.status_code == 200
        assert response.get_body().decode() == 'Welcome Mario SuperStar'

    def test_exception_post(self):
        test_post_body= 'nope'
        request = func.HttpRequest(
            method='POST',
            url='/api/azure-data-lake-gen2',
            body=test_post_body.encode('utf-8'),
            headers={
                'Content-Type':'application/json'
            }
        )
        response = post(request)
        
        assert response.status_code== 400