# vehicle_manager.py

from vehicle import Vehicle
from generate_random_vehicles import generate_vehicles_list

class VehicleManager:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_data):
        vin = vehicle_data.get('vin')
        if vin in self.vehicles:
            return {'error': 'Vehicle with this VIN already exists'}, 400
        vehicle = Vehicle(vehicle_data)
        self.vehicles[vin] = vehicle
        return str(vehicle), 201

    def get_vehicle(self, vin):
        vehicle = self.vehicles.get(vin)
        if vehicle:
            return str(vehicle), 200
        return {'error': 'Vehicle not found'}, 404

    def update_vehicle(self, vin, vehicle_data):
        vehicle = self.vehicles.get(vin)
        if not vehicle:
            return {'error': 'Vehicle not found'}, 404
        vehicle.manufacturer = vehicle_data.get('manufacturer', vehicle.manufacturer)
        vehicle.model = vehicle_data.get('model', vehicle.model)
        vehicle.year = vehicle_data.get('year', vehicle.year)
        vehicle.color = vehicle_data.get('color', vehicle.color)
        self.vehicles[vin] = vehicle
        return str(vehicle), 200

    def delete_vehicle(self, vin):
        vehicle = self.vehicles.pop(vin, None)
        if not vehicle:
            return {'error': 'Vehicle not found'}, 404
        return {'message': 'Vehicle deleted'},200

    def get_all_vehicles(self):
        return [str(vehicle) for vehicle in self.vehicles.values()]

    def get_vehicle_by_year(self, year):
        vehicles_by_year = [str(vehicle) for vehicle in self.vehicles.values() if vehicle.year == int(year)]
        if vehicles_by_year:
            return vehicles_by_year, 200
        return {'error': 'No vehicles found for this year'}, 404

    def get_vehicle_by_manufacturer(self, manufacturer):
        vehicles_by_manufacturer = [str(vehicle) for vehicle in self.vehicles.values() if vehicle.manufacturer.lower() == manufacturer.lower()]
        if vehicles_by_manufacturer:
            return vehicles_by_manufacturer, 200
        return {'error': 'No vehicles found for this manufacturer'}, 404

    def populate_with_random_vehicles(self, count=50):
        for vehicle_data in generate_vehicles_list(count):
            self.vehicles[vehicle_data['vin']] = Vehicle(**vehicle_data)

