from app.server.dashboards.dash_test.dashboard import dashboard as dash_test
from app.server.dashboards.hello_world.dashboard import dashboard as hello_world
from fastapi.routing import Mount
from a2wsgi import WSGIMiddleware

dashboards = [
    hello_world,
    dash_test,
]


def dashboard_mounts(dashboards_to_mount: list):
    return [Mount(d.get_relative_path("/"), WSGIMiddleware(d.server)) for d in dashboards_to_mount]
