from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/healthcheck/api",
)


@router.get("/ping", tags=["Health Check"])
def ping():
    """
    ---
    tags:
      - HealthCheck
    responses:
        200:
          description: "OK"
          schema:
          type: "string"
    """
    return JSONResponse(content="pong", status_code=200)
