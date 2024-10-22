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
        self.travelled_distance += self.current_speed * hours

# Create a new car object
new_car = Car("ABC-123", 142)

# Accelerate the car
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

# Print out the current speed of the car
print("Current Speed after acceleration:", new_car.current_speed, "km/h")

# Use the emergency brake
new_car.accelerate(-200)

# Print out the final speed after emergency brake
print("Final Speed after emergency brake:", new_car.current_speed, "km/h")

# Drive the car for 1.5 hours
new_car.drive(1.5)

# Print out the travelled distance
print("Travelled Distance after driving:", new_car.travelled_distance, "km")
