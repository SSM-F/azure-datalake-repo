import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpRequest:
    name = req.params.get("name")
    if name:
        return func.HttpResponse(f"Hello there, {name}!", status_code=200)
    else:
        return func.HttpResponse("PLease pass a name, dont be rude", status_code=400)