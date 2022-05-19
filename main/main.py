from fastapi import FastAPI


from .events import create_start_app_handler
from .router import router


app = FastAPI()

app.add_event_handler("startup", create_start_app_handler())

app.include_router(router)
