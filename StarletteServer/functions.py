from starlette.requests import Request
from starlette.responses import JSONResponse, Response


def hello_world(scope):
    return Response("Hello World!")


def hello_world_form_data(scope):
    async def parse(receive, send):
        request = Request(scope, receive)
        data = await request.form()
        response = JSONResponse(data['data'])
        await response(receive, send)
    return parse
