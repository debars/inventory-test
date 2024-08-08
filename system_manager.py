# system_manager.py

from system import System
from generate_random_systems import generate_systems_list

class SystemManager:
    def __init__(self):
        self.systems = {}

    def add_system(self, system_data):
        serial_number = system_data.get('serial_number')
        if serial_number in self.systems:
            return {'error': 'system with this serial number already exists'}, 400
        system = System(system_data)
        system.save_to_db()
        return str(system), 201

    def get_system(self, serial_number):
        system = self.systems.get(serial_number)
        if system:
            return str(system), 200
        return {'error': 'system not found'}, 404

    def update_system(self, serial_number, system_data):
        system = self.systems.get(serial_number)
        if not system:
            return {'error': 'system not found'}, 404
        system.location = system_data.get('location', system.location)
        system.model = system_data.get('model', system.model)
        system.name = system_data.get('year', system.name)
        self.systems[serial_number] = system
        return str(system), 200

    def delete_system(self, serial_number):
        system = self.systems.pop(serial_number, None)
        if not system:
            return {'error': 'system not found'}, 404
        return {'message': 'system deleted'},200

    def get_all_systems(self):
        systems = System.get_all_systems()
        return [str(system) for system in self.systems.values()]

    def populate_with_random_systems(self, count=50):
        for system_data in generate_systems_list(count):
            self.systems[system_data['serial_number']] = system(**system_data)

