# project/app/api/views.py


import os
import datetime
from statistics import mean, stdev
from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.api.models import SensorIn, SensorOut, SensorUpdate
from app.api.models import SystemIn, SystemOut, SystemUpdate
from app.api import db_manager
from app.api.db import sensor, system
from app.api.db import database

views = APIRouter()
templates = Jinja2Templates(directory="app/api/templates")

@views.get("/favicon.ico")
async def favicon():
    return FileResponse("app/api/static/images/favicon.ico")

@views.get("/", response_class=HTMLResponse)
def get(request: Request):
    request = {"status": "OK"}
    return templates.TemplateResponse("index.html", {"request": request})

@views.get("/sensor", response_model=List[SensorOut])
async def get_all_sensor():
    return await db_manager.get_all_sensor()

@views.get("/sensor/{_id}", response_model=SensorOut)
async def get_sensor(_id: int):
    return await db_manager.get_sensor(_id)

@views.get("/system", response_model=List[SystemOut])
async def get_all_system():
    return await db_manager.get_all_system()

@views.get("/system/{_id}", response_model=SystemOut)
async def get_system(_id: int):
    return await db_manager.get_system(_id)

@views.get("/reload", status_code=201)
async def reload(request: Request):
    # reload base data to db
    response = await db_manager.load_db()
    request = {"request": response}
    return request

@views.get("/cleanup", status_code=201)
async def cleanup(request: Request):
    # cleanup the tables
    response = await db_manager.clean_db()
    request = {"request": "OK"}
    return request

@views.get("/page/none/new", status_code=201)
async def get_page_none_new(request: Request):
    return await db_manager.get_page_none_new()

@views.get("/page/none/old", status_code=201)
async def get_page_none_old(request: Request):
    return await db_manager.get_page_none_old()

@views.get("/page/date/new", status_code=201)
async def get_page_date_new(request: Request):
    return await db_manager.get_page_date_new()

@views.get("/page/date/old", status_code=201)
async def get_page_date_old(request: Request):
    return await db_manager.get_page_date_old()

@views.get("/page/type/new", status_code=201)
async def get_page_type_new(request: Request):
    return await db_manager.get_page_type_new()

@views.get("/page/type/old", status_code=201)
async def get_page_type_old(request: Request):
    return await db_manager.get_page_type_old()

@views.get("/page/parm/new", status_code=201)
async def get_page_parm_new(request: Request):
    return await db_manager.get_page_parm_new()

@views.get("/page/parm/old", status_code=201)
async def get_page_parm_old(request: Request):
    return await db_manager.get_page_parm_old()
