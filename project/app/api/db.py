# project/app/api/db.py

import os

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    MetaData,
    ForeignKey,
    String,
    Boolean,
    Table,
    create_engine,
    ARRAY,
    Float,
)
from sqlalchemy.sql import func

from databases import Database

from app.config import config

DATABASE_URL = config.database_url

engine = create_engine(DATABASE_URL)
metadata = MetaData()

sensor = Table(
    "sensor",
    metadata,
    Column("sensorId", Integer, primary_key=True),
    Column("name", String(256)),
    Column("location", String(256)),
    Column("model", String(256)),
    Column("serial_number", String(256)),
)

system = Table(
    "system",
    metadata,
    Column("systemId", Integer, primary_key=True),
    Column("name", String(256)),
    Column("contact", String(256)),
    Column("location", String(256)),
    Column("asset_tag", String(256)),
    Column("model", String(256)),
    Column("serial_number", String(256)),
    Column("mac_address", String(256)),
    Column("ip_address", String(256)),
)

database = Database(DATABASE_URL)
