#!/usr/bin/python
# -*- coding: utf-8 -*-

from .routes.middleware import metrics_app, AddProcessTimeHeaderMiddleware
# from starlette.middleware.sessions import SessionMiddleware
from .routes import docs, health
from .message import *
from .config import settings
from fastapi import FastAPI, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .exceptions import CacheException, ConflictException, NotFoundException, UnauthorizedException, InvalidValueException
from fastapi.responses import JSONResponse
from tian_core.logger import logger
import traceback

def create_fast_api_service(
    service_name: str = "default",
    config_cls: list = None,
    enable_cors: bool = False,
    lifespan: callable = None,
):
    """
    Create a new FastAPI application instance.
    """
    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )
    
    app = FastAPI(
        title=service_name,
        # contact={},
        # # root_path="/api/v1",
        # version="2.1.0",
        # root_path_in_servers=False,
        # docs_url=None,  # disable default docs
        # redoc_url=None,  # disable default redoc
        # openapi_url="/openapi.json",  # still serve OpenAPI schema
        # summary="",
        lifespan=lifespan,
    )

    app.mount("/_/metrics", app=metrics_app)
    app.add_middleware(AddProcessTimeHeaderMiddleware)
    # app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
    app.include_router(docs.router, prefix="/_", tags=["Systems"])
    app.include_router(health.router, prefix="/_", tags=["Systems"])

    @app.exception_handler(CacheException)
    async def cache_exception_handler(request: Request, exc: CacheException):
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(message="Cache error", error=str(exc), data=None).dict()
        )

    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc: NotFoundException):
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(message="Not Found", error=str(exc), data=None).dict()
        )

    @app.exception_handler(ConflictException)
    async def conflict_handler(request: Request, exc: ConflictException):
        return JSONResponse(
            status_code=409,
            content=ErrorResponse(message="Conflict", error=str(exc), data=None).dict()
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized_handler(request: Request, exc: UnauthorizedException):
        return JSONResponse(
            status_code=401,
            content=ErrorResponse(message="Unauthorized", error=str(exc), data=None).dict()
        )
    
    @app.exception_handler(InvalidValueException)
    async def invalid_value_handler(request: Request, exc: InvalidValueException):
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(message="Invalid Value", error=str(exc), data=None).dict()
        )
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        # Log traceback for debugging (optional)
        logger.critical(f"Unhandled exception: {traceback.format_exc()}")

        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                message="Internal server error",
                error=str(exc),
                data=None
            ).dict()
        )
    return app
    


