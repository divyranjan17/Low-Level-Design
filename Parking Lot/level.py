from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle

class Level:
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(num_spots)] # initialize ParkingSpot instance with a number

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                print(f"Vehicle {vehicle.get_license_plate()} parked successfully at spot number {spot.get_spot_number()} located on level {self.floor}")
                return True
        return False
        
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle == vehicle:
                spot.unpark_vehicle()
                print(f"Vehicle {vehicle.get_license_plate()} unparked successfully from spot number {spot.get_spot_number()} located on level {self.floor}")
                return True
        return False
    
    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parking_spots:
            if spot.is_available():
                print(f"Spot {spot.get_spot_number()} availability: {'Available' if spot.is_available() else 'Occupied'}")