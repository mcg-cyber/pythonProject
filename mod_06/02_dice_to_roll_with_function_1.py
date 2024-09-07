import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice (e.g., 6 for a standard dice): "))

    max_value = sides  # The maximum value when rolling the dice is equal to the number of sides.

    while True:
        result = roll_dice(sides)
        print(f'You rolled: {result}')
        if result == max_value:
            print(f'You rolled a {max_value}! Stopping the rolls.')
            break

if __name__ == "__main__":
    main()
