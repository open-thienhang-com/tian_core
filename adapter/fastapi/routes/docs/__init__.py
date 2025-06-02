from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()
custom_logo_url = "https://thienhang.com/images/thienhang.com-black.svg"
service_name = "MyService"  # <- Bạn nên truyền từ config

@router.get("/", include_in_schema=False)
async def custom_home(request: Request):
    if request.cookies.get("auth") != "ok":
        return RedirectResponse("/login")

    html = get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=service_name,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    ).body.decode()

    # Inject custom header + footer
    html += f"""
    <style> /* [CUSTOM STYLES] */ </style>
    <div class="custom-nav"> ... </div>
    <div class="custom-footer"> ... </div>
    """
    return HTMLResponse(content=html, status_code=200)


@router.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def custom_docs(request: Request):
    if request.cookies.get("auth") != "ok":
        return RedirectResponse("/login")
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=service_name + " - Docs"
    )


@router.get("/redoc", response_class=HTMLResponse, include_in_schema=False)
async def custom_redoc(request: Request):
    if request.cookies.get("auth") != "ok":
        return RedirectResponse("/login")
    return get_redoc_html(
        openapi_url="/openapi.json",
        title=service_name + " - ReDoc"
    )


@router.get("/openapi.json", include_in_schema=False)
async def custom_openapi(request: Request):
    if request.cookies.get("auth") != "ok":
        return RedirectResponse("/login")
    return request.app.openapi()
