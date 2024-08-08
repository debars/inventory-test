from pydantic import BaseModel
import sqlite3

class System(BaseModel):
    name: str
    contact: str
    location: str
    asset_tag: str
    serial_number: str
    model_number: str
    mac_address: str
    ip_address: str

    def __init__(self, **data):
        super().__init__(**data)
        self.name = data['name']
        self.contact = data['contact']
        self.location = data['location']
        self.asset_tag = data['asset_tag']
        self.serial_number = data['serial_number']
        self.model_number = data['model_number']
        self.mac_address = data['mac_address']
        self.ip_address = data['ip_address']

    def __repr__(self):
        return (f'Name: {self.name}, Contact: {self.contact}, Location: {self.location}, '
                f'asset tag: {self.asset_tag}, serial_number: {self.serial_number}, '
                f'Model: {self.model_number}, MAC Address: {self.mac_address}, IP Address: {self.ip_address}')

    def __str__(self):
        return self.__repr__()

    def save_to_db(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO systems (name, contact, location, asset_tag, serial_number, model_number, mac_address, ip_address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.name, self.contact, self.location, self.asset_tag, self.serial_number, self.model_number, self.mac_address, self.ip_address))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_all_systems():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM systems')
        systems = cursor.fetchall()
        conn.close()
        return systems