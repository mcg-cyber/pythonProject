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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            acceleration = random.randint(-10, 15)  # Random acceleration between -10 and +15 km/h
            car.accelerate(acceleration)
            car.drive(1)  # Drive for 1 hour

    def print_status(self):
        print("\nCurrent Race Status:")
        print("Registration Number | Maximum Speed (km/h) | Current Speed (km/h) | Travelled Distance (km)")
        print("-" * 80)
        for car in self.cars:
            print(f"{car.registration_number:<20} | {car.maximum_speed:<20} | {car.current_speed:<20} | {car.travelled_distance:<30}")
        print()  # Empty line for better readability

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

# Example usage
car_list = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Prix", 10000, car_list)

while not race.race_finished():
    race.hour_passes()
    race.print_status()

print("The race is finished!")
