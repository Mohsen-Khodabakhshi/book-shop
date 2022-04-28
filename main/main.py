from fastapi import FastAPI

from main.router import router

app = FastAPI()

app.include_router(router)

