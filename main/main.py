from fastapi import FastAPI


from .events import create_start_app_handler, config_jwt_auth
from .router import router


app = FastAPI()

app.add_event_handler("startup", create_start_app_handler())

config_jwt_auth(app)

app.include_router(router)

