# Vehicle Management System

## To Run:

1. Create a virtual environment:
    ```bash
    python -m venv env
    ```
2. Activate the virtual environment:
    ```bash
    . env/bin/activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Console Output Only
This invocation will provide a console output only with options to add, delete, update, list, get by VIN, list by year, list by manufacturer :
```bash
python main.py --console
```

### FastAPI
This invocation will provide a FastAPI with the following endpoints described below:
```bash
python main.py
```

## API Endpoints
Visit [http://localhost:8000/docs](http://localhost:8000/docs)

- This will provide an interface to perform the following:
    - View a list of all vehicles.
    - Add a new vehicle.
    - Get a vehicle by VIN.
    - Update a vehicle by VIN.
    - Delete a vehicle by VIN.
    - View a list of vehicles by year.
    - View a list of vehicles by manufacturer.

