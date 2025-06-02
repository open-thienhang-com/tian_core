try:
    from .fastapi import create_fast_api_service
    from .fastapi.config import settings
    from .fastapi.message import *
except ImportError as e:
    create_fast_api_service = None
    print(f"FastAPI service not available. Ensure 'fastapi' is installed. {e}")

try:
    from .flask import FlaskBaseService
except ImportError:
    FlaskBaseService = None