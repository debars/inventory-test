from pydantic import BaseModel

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
        return (f'Name: {self.name}, f'Location: {self.location}, '
                f'serial_number: {self.serial_number}, Model: {self.model}')

    def __str__(self):
        return self.__repr__()