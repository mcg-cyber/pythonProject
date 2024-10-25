import random
from mod_10._04_car_class import Car, Race

def main():
    # Create a list of 10 car objects with random maximum speeds between 100 km/h and 200 km/h
    car_list = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_number = f"ABC-{i}"
        car = Car(reg_number, max_speed)
        car_list.append(car)

    # Create a race instance with a name, distance, and the list of cars
    race = Race("Grand Demolition Derby", 8000, car_list)

    # Simulate the race until one of the cars has advanced the entire distance
    hour = 0
    while not race.race_finished():
        hour += 1
        race.hour_passes()
        if hour % 10 == 0:
            print(f"Hour {hour} of the race:")
            race.print_status()
            print()  # Empty line for better readability between status updates

    # Print the final results
    print("\nFinal Race Results:")
    race.print_status()

if __name__ == "__main__":
    main()
