
import random
import string

def generate_random_vin():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))

def generate_random_manufacturer():
    makes = ['Toyota', 'Ford', 'Chevrolet', 'Honda', 'Nissan', 'BMW', 'Mercedes', 'Volkswagen', 'Audi', 'Hyundai', 'Tesla']
    return random.choice(makes)

def generate_random_model():
    models = ['Sedan', 'SUV', 'Truck', 'Coupe', 'Hatchback', 'Convertible', 'Wagon', 'Van']
    return random.choice(models)

def generate_random_year():
    return random.randint(2000, 2024)

def generate_random_color():
    colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Gray', 'Silver', 'Yellow', 'Brown', 'Orange']
    return random.choice(colors)

def generate_random_vehicle():
    return {
        'vin': generate_random_vin(),
        'manufacturer': generate_random_manufacturer(),
        'model': generate_random_model(),
        'year': generate_random_year(),
        'color': generate_random_color()
    }

def generate_vehicles_list(n=50):
    return [generate_random_vehicle() for _ in range(n)]
