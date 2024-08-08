class Console:
    def __init__(self, vehicle_manager):
        self.vehicle_manager = vehicle_manager
        self.commands = {
            'add': {'prompt': 'Enter vehicle data as JSON: ', 'command': self.add_vehicle},
            'get': {'prompt': 'Enter VIN: ', 'command': self.get_vehicle},
            'update': {'prompt': 'Enter VIN: ', 'command': self.update_vehicle},
            'delete': {'prompt': 'Enter VIN: ', 'command': self.delete_vehicle},
            'list': {'prompt': '', 'command': self.list_vehicles},
            'year': {'prompt': 'Enter year: ', 'command': self.get_vehicle_by_year},
            'manufacturer': {'prompt': 'Enter manufacturer: ', 'command': self.get_vehicle_by_manufacturer},
            'exit': {'prompt': '', 'command': self.exit_console}
        }
        self.running = True

    def add_vehicle(self, data):
        result, status = self.vehicle_manager.add_vehicle(eval(data))
        if status == 201:
            print(result)
        else:
            print(result['error'])

    def get_vehicle(self, vin):
        result, status = self.vehicle_manager.get_vehicle(vin)
        if status == 200:
            print(result)
        else:
            print(result['error'])

    def update_vehicle(self, vin):
        data = input("Enter updated vehicle data as JSON: ")
        result, status = self.vehicle_manager.update_vehicle(vin, eval(data))
        if status == 200:
            print(result)
        else:
            print(result['error'])

    def delete_vehicle(self, vin):
        result, status = self.vehicle_manager.delete_vehicle(vin)
        if status == 200:
            print(result)
        else:
            print(result['error'])

    def list_vehicles(self, _):
        vehicles = self.vehicle_manager.get_all_vehicles()
        for vehicle in vehicles:
            print(vehicle)

    def get_vehicle_by_year(self, year):
        result, status = self.vehicle_manager.get_vehicle_by_year(year)
        if status == 200:
            for vehicle in result:
                print(vehicle)
        else:
            print(result['error'])

    def get_vehicle_by_manufacturer(self, manufacturer):
        result, status = self.vehicle_manager.get_vehicle_by_manufacturer(manufacturer)
        if status == 200:
            for vehicle in result:
                print(vehicle)
        else:
            print(result['error'])

    def exit_console(self, _):
        self.running = False

    def run(self):
        while self.running:
            command = input("Enter command (add, get, update, delete, list, year, manufacturer, exit): ").strip().lower()
            if command in self.commands:
                prompt = self.commands[command]['prompt']
                if prompt:
                    data = input(prompt)
                    self.commands[command]['command'](data)
                else:
                    self.commands[command]['command'](None)
            else:
                print("Unknown command")

