from typing import List, Dict
from level import Level
from vehicle import Vehicle
from parking_spot import ParkingSpot

class ParkingLot:
    _instance = None
    
    def __init__(self):
        self.levels: List[Level] = []

    @staticmethod
    def get_parking_lot(): # applying Singleton pattern
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> None:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def add_level(self, level: Level) -> None:
        self.levels.append(level)

    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()

