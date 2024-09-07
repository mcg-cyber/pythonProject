# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.

import random


def roll_dice(sides=6):
    return random.randint(1, sides)


def main():
    sides = 6

    while True:
        result = roll_dice(sides)
        print(result)
        if result == 6:
            break


if __name__ == "__main__":
    main()
