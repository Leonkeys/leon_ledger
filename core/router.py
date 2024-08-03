from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.menu import router as menu_router
from core.config import settings

api_router = APIRouter()


@api_router.get('/', include_in_schema=False)
async def index():
    return RedirectResponse(url=settings.DOCS_URL)


api_router.include_router(menu_router, prefix="/menu", tags=["菜单"])

__all__ = ["api_router"]
