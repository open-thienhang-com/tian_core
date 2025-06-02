import os
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from ...config import settings

from fastapi import Request
from tian_core.logger import logger
import time

import prometheus_client as prometheus
from prometheus_client import make_asgi_app

os.environ["TZ"] = "Asia/Ho_Chi_Minh"

# Initialize the metrics
counter = prometheus.Counter(
    name="tian_http_request_rates",
    documentation="Track the total number of requests",
    labelnames=[
        "service_name",
        "http_method",
        "endpoint",
        "http_status_code",
        "error_code",
    ],
)

histogram = prometheus.Histogram(
    name="tian_http_request_duration_seconds",
    documentation="Track the duration of requests in seconds",
    # buckets=[0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 5, 10],
    labelnames=[
        "service_name",
        "http_method",
        "endpoint",
        "http_status_code",
        "error_code",
    ],
)


metrics_app = make_asgi_app()


class AddProcessTimeHeaderMiddleware(BaseHTTPMiddleware):
    """Middleware to measure request processing time and add it to headers"""

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        logger.debug(
            f"Request {request.url} received at {start_time} body: {await request.body()}"
        )
        response: Response = await call_next(request)

        # if request.url.path in settings.path_metrics:
        #     process_time = time.time() - start_time
        #     response.headers["X-REC-Process-Time"] = str(round(process_time, 4))
        #     response.headers["Cache-Control"] = "public, max-age=0"
        #     if round(process_time, 4) > 0.1:
        #         logger.warning(
        #             f"SLOW Request {request.url}  | Process time: {process_time}"
        #         )
        #     else:
        #         logger.debug(f"Request {request.url}  | Process time: {process_time}")
        #     counter.labels(
        #         service_name=settings.app.service_short_name,
        #         http_method=request.method,
        #         endpoint=request.url.path,
        #         http_status_code=response.status_code,
        #         error_code=response.status_code,
        #     ).inc()

        #     histogram.labels(
        #         service_name=settings.app.service_short_name,
        #         http_method=request.method,
        #         endpoint=request.url.path,
        #         http_status_code=response.status_code,
        #         error_code=response.status_code,
        #     ).observe(process_time)
        return response
