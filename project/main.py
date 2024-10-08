# project/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.views import views
from app.api.db import metadata, database, engine


metadata.create_all(engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/api/static"), name="static")

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(views)
