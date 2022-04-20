from fastapi import FastAPI

from apps.main.router import router

app = FastAPI()

app.include_router(router)

