from vehicle import Vehicle
from vehicle_type import VehicleType

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(VehicleType.CAR, license_plate)