import random
from mod_10_04_car_class_continues import Car, Race

def main():
    # Create a list of 10 car objects with random maximum speeds between 100 km/h and 200 km/h
    car_list = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    # Create a race instance
    race = Race("Grand Demolition Derby", 8000, car_list)

    # Simulate the race
    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        # Print status every 10 hours
        if hours_passed % 10 == 0:
            race.print_status()

    # Print final status
    race.print_status()
    print("The race is finished!")

if __name__ == "__main__":
    main()
