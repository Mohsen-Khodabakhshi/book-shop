from fastapi import APIRouter

from apps.user.controller import UserController
from apps.user.schema import TestSchemaOut

client_router = APIRouter()


@client_router.get("/", response_model=TestSchemaOut)
async def main(name: str = "Mohsen"):
    return await UserController().main(name)
