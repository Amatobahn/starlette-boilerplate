from starlette.applications import Starlette
import uvicorn


class Route(object):
    def __init__(self, path: str, func, methods):
        self.path = path
        self.function = func
        self.methods = methods


class Routes(object):
    def __init__(self, routes=None):
        self.routes = list() if routes is None else routes

    def add_route(self, route: Route):
        self.routes.append(route)


class StarletteServer(object):
    def __init__(self, ip: str="127.0.0.1", port: int=8080, debug: bool=False):
        self.server = Starlette(debug=debug)
        self.ip = ip
        self.port = port

    def add_routes(self, routes: Routes):
        for route in routes.routes:
            self.add_route(route)

    def add_route(self, route: Route):
        self.server.add_route(route.path, route.function, route.methods)

    def run(self):
        uvicorn.run(self.server, host=self.ip, port=self.port)
