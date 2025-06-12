#!/usr/bin/python
# -*- coding: utf-8 -*-

from .routes.middleware import metrics_app, AddProcessTimeHeaderMiddleware
# from starlette.middleware.sessions import SessionMiddleware
from .routes import docs, health
from .message import *
from .config import settings
from fastapi import FastAPI
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

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
    return app
    


