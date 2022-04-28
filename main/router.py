from fastapi import APIRouter

from apps.user.api.client import client_router as user_client_router

router = APIRouter()

router.include_router(
    user_client_router,
    prefix="/user",
    tags=["user-client"],
)

