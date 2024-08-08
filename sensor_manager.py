# sensor_manager.py

from sensor import Sensor
from generate_random_sensors import generate_sensors_list

class SensorManager:
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, sensor_data):
        serial_number = sensor_data.get('serial_number')
        if serial_number in self.sensors:
            return {'error': 'sensor with this serial number already exists'}, 400
        sensor = Sensor(sensor_data)
        sensor.save_to_db()
        return str(sensor), 201

    def get_sensor(self, serial_number):
        sensor = self.sensors.get(serial_number)
        if sensor:
            return str(sensor), 200
        return {'error': 'sensor not found'}, 404

    def update_sensor(self, serial_number, sensor_data):
        sensor = self.sensors.get(serial_number)
        if not sensor:
            return {'error': 'sensor not found'}, 404
        sensor.location = sensor_data.get('location', sensor.location)
        sensor.model = sensor_data.get('model', sensor.model)
        sensor.name = sensor_data.get('year', sensor.name)
        self.sensors[serial_number] = sensor
        return str(sensor), 200

    def delete_sensor(self, serial_number):
        sensor = self.sensors.pop(serial_number, None)
        if not sensor:
            return {'error': 'sensor not found'}, 404
        return {'message': 'sensor deleted'},200

    def get_all_sensors(self):
        sensors = Sensor.get_all_sensors()
        return [str(sensor) for sensor in self.sensors.values()]

    def populate_with_random_sensors(self, count=50):
        for sensor_data in generate_sensors_list(count):
            self.sensors[sensor_data['serial_number']] = sensor(**sensor_data)

