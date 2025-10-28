class vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return f"vehicle_id: {self._vehicle_id}, Base Rate: {self._base_rate}"
    
    def rental_charge(self):
        return 0.0
    
class car(vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
            super().__init__(vehicle_id, base_rate)
            self.num_seats = num_seats

    def rental_charge(self):
            return self._base_rate * self.num_seats
        
class bike(vehicle):
     def __init__(self, vehicle_id, base_rate, bike_type):
          super().__init__(vehicle_id, base_rate)
          self.bike_type = bike_type

     def rental_charge(self):
        return self._base_rate * 0.5
     
def calculate_rental(vehicle):
    return vehicle.rental_charge()


if __name__ == "__main__":
    car1 = car("CAR001", 100.00, 4)
    bike1 = bike("BIKE001", 500.0, "Motorcycle")

    print(car1.display_details())
    print(f"Car Rental Charge: ₹{calculate_rental(car1):.2f}")

    print(bike1.display_details())
    print(f"Bike Rental Charge: ₹{calculate_rental(bike1):.2f}")
     

     


    

