from StarletteServer.server import StarletteServer, Routes, Route
from StarletteServer.functions import *


def main():
    routes = Routes()
    routes.add_route(Route("/", hello_world, ['GET']))
    routes.add_route(Route("/form/", hello_world_form_data, ['POST']))

    app = StarletteServer(debug=True)
    app.add_routes(routes)
    app.run()


if __name__ == "__main__":
    main()

