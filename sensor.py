from pydantic import BaseModel
import sqlite3

class Sensor(BaseModel):
    name: str
    location: str
    model: str
    serial_number: str

    def __init__(self, **data):
        super().__init__(**data)
        self.name = data['name']
        self.model = data['model']
        self.location = data['location']
        self.serial_number = data['serial_number']

    def __repr__(self):
        return (f'Name: {self.name}, Location: {self.location}, '
                f'serial_number: {self.serial_number}, Model: {self.model}')

    def __str__(self):
        return self.__repr__()

    def save_to_db(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sensors (name, location, model, serial_number)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.location, self.model, self.serial_number))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_sensors():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sensors')
        sensors = cursor.fetchall()
        conn.close()
        return sensors