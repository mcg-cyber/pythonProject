import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

def main():
    # Create one electric car and one gasoline car
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Set speeds for both cars
    electric_car.accelerate(150)
    gasoline_car.accelerate(140)

    # Make them drive for three hours
    electric_car.drive(3)
    gasoline_car.drive(3)

    # Print out the values of their kilometer counters
    print(f"Electric Car {electric_car.registration_number} - Travelled Distance: {electric_car.travelled_distance} km")
    print(f"Gasoline Car {gasoline_car.registration_number} - Travelled Distance: {gasoline_car.travelled_distance} km")

if __name__ == "__main__":
    main()
