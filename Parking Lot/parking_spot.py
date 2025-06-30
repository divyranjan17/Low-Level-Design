from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, num: int):
        self.spot_number = num
        self.vehicle_type = VehicleType.CAR # default value
        self.parked_vehicle = None
    
    def is_available(self) -> bool:
        return self.parked_vehicle is None
    
    def get_spot_number(self) -> int:
        return self.spot_number
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    
    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle
    
    def park_vehicle(self, vehicle: Vehicle) -> None:
        self.parked_vehicle = vehicle
    
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None