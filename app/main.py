"""FastGeoflow - Geoflow"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.routers.geoflow import router as geoflow_router

DESCRIPTION = """
A lightweight python api to run geoworkflows.
"""

app = FastAPI(
    title="FastVector",
    description=DESCRIPTION,
    version="0.0.1",
    contact={
        "name": "Michael Keller",
        "email": "michaelkeller03@gmail.com",
    },
    license_info={
        "name": "The MIT License (MIT)",
        "url": "https://mit-license.org/",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    geoflow_router.router,
    prefix="/api/v1/geoflow",
    tags=["import"],
)

Instrumentator().instrument(app).expose(app)
