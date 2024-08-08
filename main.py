# main.py

import sys
import argparse
from fastapi import FastAPI, HTTPException
from sensor import Sensor
from sensor_manager import SensorManager
from console import Console

# Create the flask app.
app = FastAPI()

# Utilize the sensor manager to handle sensor access.
sensor_manager = SensorManager()

@app.get('/sensors')
def get_sensors():
    sensors = sensor_manager.get_all_sensors()
    return sensors

# Add a sensor (POST)
# http://localhost:8000/sensor
@app.post('/sensor')
def add_sensor(sensor: sensor):
    sensor, status = sensor_manager.add_sensor(sensor.dict())
    if status != 201:
        raise HTTPException(status_code=status, detail=new_sensor['error'])
    return sensor

@app.get('/sensor/{sn}')
def get_sensor(sn: str):
    sensor, status = sensor_manager.get_sensor(sn)
    if status != 200:
        raise HTTPException(status_code=status, detail=sensor['error'])
    return sensor
    
@app.put('/sensor/{sn}')
def update_sensor(sn: str, sensor: sensor):
    sensor, status = sensor_manager.update_sensor(sn, sensor.dict())
    if status != 200:
        raise HTTPException(status_code=status, detail=sensor['error'])
    return sensor

@app.delete('/sensor/{sn}')
def delete_sensor(sn: str):
    message, status = sensor_manager.delete_sensor(sn)
    if status != 200:
        raise HTTPException(status_code=status, detail=message['error'])
    return message
    
if __name__ == '__main__':
    # Create an initial random list of sensors, 50 by default.
    # Add a different number as a parameter to change the number of sensors.
    sensor_manager.populate_with_random_sensors()

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
