from time import process_time
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from logger.logger import logger

class Errorhandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, ) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response or JSONResponse: # type: ignore
        try:
            url_service = str(request.url)
            url_service = url_service.replace(str(request.base_url), '')
            response = await call_next (request)
            logger.info(f"Successfull: status_code: {response.status_code}, service: '{url_service}', method: '{request.method}', time: {process_time()}")
            return response
        except Exception as e:
            url_service = str(request.url)
            url_service = url_service.replace(str(request.base_url), '')
            logger.error(f"Error: service: '{url_service}', method: '{request.method}', time: {process_time()}")
            return JSONResponse(status_code=500, content={"error":str(e)})