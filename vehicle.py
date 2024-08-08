from pydantic import BaseModel

class Vehicle(BaseModel):
    vin: str
    manufacturer: str
    model: str
    year: int
    color: str

    def __init__(self, **vehicle_data):
        super().__init__(**vehicle_data)
        self.vin = vehicle_data['vin']
        self.manufacturer = vehicle_data['manufacturer']
        self.model = vehicle_data['model']
        self.color = vehicle_data['color']
        self.year = vehicle_data['year']

    def __repr__(self):
        return (f'VIN: {self.vin}, Manufacturer: {self.manufacturer}, '
                f'Model: {self.model}, Year: {self.year}, Color: {self.color}')

    def __str__(self):
        return self.__repr__()