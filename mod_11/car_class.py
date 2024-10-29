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
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def simulate_race(self):
        target_distance = 10000
        hour = 0
        while all(car.travelled_distance < target_distance for car in self.cars):
            hour += 1
            print(f"Hour {hour} of the race:")
            for car in self.cars:
                acceleration = random.randint(-10, 15)  # Random acceleration between -10 and +15 km/h
                car.accelerate(acceleration)
                car.drive(1)  # Drive for 1 hour
                print(f"Car {car.registration_number} - Current Speed: {car.current_speed} km/h, Travelled Distance: {car.travelled_distance} km")
            print()  # Empty line for better readability between hours

        # Print the properties of each car in a clear table format
        print("\nRace Results:")
        print("Registration Number | Maximum Speed (km/h) | Final Speed (km/h) | Travelled Distance (km)")
        print("-" * 80)
        for car in self.cars:
            print(f"{car.registration_number:<20} | {car.maximum_speed:<20} | {car.current_speed:<20} | {car.travelled_distance:<30}")

# Create a list of 10 car objects with random maximum speeds between 100 km/h and 200 km/h and registration numbers as "ABC-1", "ABC-2", and so on
car_list = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    reg_number = f"ABC-{i}"
    car = Car(reg_number, max_speed)
    car_list.append(car)

# Create a race instance
race = Race()

# Add cars to the race
for car in car_list:
    race.add_car(car)

# Simulate the race until one of the cars has advanced at least 10,000 kilometers
race.simulate_race()
