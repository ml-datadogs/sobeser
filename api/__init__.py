import random

from fastapi import FastAPI

from api import config as cfg
from api import utils

app = FastAPI()


@app.get("/healthcheck")
async def read_root():
    return {"status": "ok"}


@app.get("/creds/{service_name}")
async def get_creds(api_key: str, service_name: str):
    if api_key != cfg.API_KEY:
        return {'status': 'not_authorized'}

    status_payload = (
        {"status": "success"}
        if service_name in cfg.SERVICE_X_CREDS.keys()
        else {"status": "no_such_service"}
    )
    return {
        "requested_service": service_name,
        **status_payload,
        "credentials": cfg.SERVICE_X_CREDS.get(service_name, {}),
    }


@app.get("/sales")
async def get_sales(api_key: str):
    if api_key != cfg.API_KEY:
        return {'status': 'not_authorized'}

    if random.randint(0, 10) <= 3:
        return {**utils.generate_sales_entry(), "status": "success"}
    else:
        return {"status": "no_new_sales"}
