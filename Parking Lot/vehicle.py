from vehicle_type import VehicleType
from abc import ABC

class Vehicle(ABC):
    def __init__(self, vehicle_type: VehicleType, license_plate: str):
        self.type = vehicle_type
        self.license_plate = license_plate

    def get_license_plate(self):
        return self.license_plate
    
    def get_type(self):
        return self.type