# project/app/api/db_manager.py

import os
import datetime

from sqlalchemy import and_
from sqlalchemy import desc, asc
from sqlalchemy import join
from sqlalchemy import text

from app.api.models import SensorIn, SensorOut, SensorUpdate
from app.api.models import SystemIn, SystemOut, SystemUpdate
from app.api.db import sensor, system
from app.api.db import database


async def add_sensor(payload: SensorIn):
    query = sensor.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_sensor():
    query = sensor.select().order_by("sensorId")
    return await database.fetch_all(query=query)

async def get_sensor(id):
    query = sensor.select(sensor.c.sensorId == id)
    return await database.fetch_one(query=query)

async def delete_sensor(id: int):
    query = sensor.delete().where(sensor.c.sensorId == id)
    return await database.execute(query=query)

async def update_sensor(id: int, payload: SensorIn):
    query = sensor.update().where(sensor.c.sensor == id).values(**payload.dict())
    return await database.execute(query=query)

async def add_system(payload: SystemIn):
    query = system.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_system():
    query = system.select().order_by("systemId")
    return await database.fetch_all(query=query)

async def get_system(id):
    query = system.select(system.c.systemId == id)
    return await database.fetch_one(query=query)

async def delete_system(id: int):
    query = system.delete().where(system.c.systemId == id)
    return await database.execute(query=query)

async def update_system(id: int, payload: SystemIn):
    query = system.update().where(system.c.system == id).values(**payload.dict())
    return await database.execute(query=query)

async def load_db():
    response = []

    sensor = {
       "name": "Sensor #1",
       "location": "office",
       "model": "WiNG-T",
       "serial_number": "63B94BC5",
    }
    response.append(sensor)
    sensor_in_db = SensorIn(**sensor)
    data = await add_sensor(sensor_in_db)

    system = {
       "name": "Sensor #1",
       "contact": "Alan",
       "location": "office",
       "asset_tag": "none",
       "model": "WiNG-MGR v2",
       "serial_number": "7",
       "mac_address": "00:90:5B:FE:09:08",
       "ip_address": "10.0.0.165",
    }
    response.append(system)
    system_in_db = SystemIn(**system)
    data = await add_system(system_in_db)

    return response

async def init_db():
    response = await load_db()
    return response

async def clean_db():
    # cleanup the tables
    query = sensor.delete()
    response = await database.execute(query=query)
    query = system.delete()
    response = await database.execute(query=query)
    return response

async def get_page_none_new():
    pass

async def get_page_none_old():
    pass

async def get_page_date_new():
    pass

async def get_page_date_old():
    pass

async def get_page_type_new():
    pass

async def get_page_type_old():
    pass

async def get_page_parm_new():
    pass

async def get_page_parm_old():
    pass
