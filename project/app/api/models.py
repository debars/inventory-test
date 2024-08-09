# project/app/api/models.py

import datetime
from pydantic import BaseModel
from typing import List, Optional


class SensorIn(BaseModel):
    name: str
    location: str
    model: str
    serial_number: str

class SensorOut(SensorIn):
    sensorId: int

class SensorUpdate(SensorIn):
    name: Optional[str] = None
    location: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None

class SystemIn(BaseModel):
    name: str
    contact: str
    location: str
    asset_tag: str
    serial_number: str
    model: str
    mac_address: str
    ip_address: str

class SystemOut(SystemIn):
    systemId: int

class SystemUpdate(SensorIn):
    name: Optional[str] = None
    contact: Optional[str] = None
    location: Optional[str] = None
    asset_tag: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    mac_address: Optional[str] = None
    ip_address: Optional[str] = None

