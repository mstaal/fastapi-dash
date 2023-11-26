from pydantic import BaseSettings


class APPSettings(BaseSettings):

    # logging and instrumentation
    log_level: str = "DEBUG"
    log_json: int = 0
    log_file_path: str = None
    instrumentation_enabled: bool = True
    instrumentation_default_metrics: bool = True
    instrumentation_prefix_all_metrics: bool = False

    # app
    fast_api_app_name: str = "fastapi-dash"
    fast_api_app_version: str = "0.0.0.1"
    fast_api_debug: bool = True
    fast_api_docs_url: str = "/fastapi-dash/apidocs"
    fast_api_redoc_url: str = "/redoc"

    # api
    api_build_number: str = None
    api_host: str = "0.0.0.0"
    api_port: int = 20409
    dashboards_tenant: str = None
    dashboards_client_id: str = None
    dashboards_client_secret: str = None
    dashboards_session_secret: str = None


app_settings = APPSettings()
