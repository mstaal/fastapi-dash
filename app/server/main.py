from app.server import app_settings
from app.server.api import health_check_endpoints
from app.server.dashboards.landingpage.dashboard import dashboard as landingpage
from app.server.dashboards.mounts import dashboard_mounts, dashboards
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

# Define the FastAPI server
app = FastAPI(
    middleware=[
        Middleware(SessionMiddleware, secret_key=app_settings.dashboards_session_secret),
    ],
    routes=dashboard_mounts(dashboards + [landingpage]),
)


# Define the main API endpoint
@app.get("/")
def index():
    return RedirectResponse(url=landingpage.get_relative_path("/"))


# Add additional FastAPI endpoints
app.include_router(health_check_endpoints.router, dependencies=[])
