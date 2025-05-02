import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if name:
        return func.HttpResponse(f"Hello there, {name}!", status_code=200)
    else:
        return func.HttpResponse("Please pass a name, dont be rude", status_code=400)
    

def post(req:func.HttpRequest)-> func.HttpResponse:
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON",status_code=400)
    name = data.get('name')
    surname = data.get('surname')
    return func.HttpResponse(f"Welcome {name} {surname}", status_code=200)
