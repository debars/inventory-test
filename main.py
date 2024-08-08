# main.py

import sys
import argparse
from fastapi import FastAPI, HTTPException
from vehicle import Vehicle
from vehicle_manager import VehicleManager
from console import Console

# Create the flask app.
app = FastAPI()

# Utilize the vehicle manager to handle vehicle access.
vehicle_manager = VehicleManager()

@app.get('/vehicles')
def get_vehicles():
    vehicles = vehicle_manager.get_all_vehicles()
    return vehicles

# Add a vehicle (POST)
# http://localhost:8000/vehicle
@app.post('/vehicle')
def add_vehicle(vehicle: Vehicle):
    vehicle, status = vehicle_manager.add_vehicle(vehicle.dict())
    if status != 201:
        raise HTTPException(status_code=status, detail=new_vehicle['error'])
    return vehicle

@app.get('/vehicle/{vin}')
def get_vehicle(vin: str):
    vehicle, status = vehicle_manager.get_vehicle(vin)
    if status != 200:
        raise HTTPException(status_code=status, detail=vehicle['error'])
    return vehicle
    
@app.put('/vehicle/{vin}')
def update_vehicle(vin: str, vehicle: Vehicle):
    vehicle, status = vehicle_manager.update_vehicle(vin, vehicle.dict())
    if status != 200:
        raise HTTPException(status_code=status, detail=vehicle['error'])
    return vehicle

@app.delete('/vehicle/{vin}')
def delete_vehicle(vin: str):
    message, status = vehicle_manager.delete_vehicle(vin)
    if status != 200:
        raise HTTPException(status_code=status, detail=message['error'])
    return message
    
if __name__ == '__main__':
    # Create an initial random list of vehicles, 50 by default.
    # Add a different number as a parameter to change the number of vehicles.
    vehicle_manager.populate_with_random_vehicles()

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
