# This script chooses a number between 1 and 10
# and then asks the user to guess it. If the user eneters the correct number then program exits

import random

num = random.randint(1, 10)
print(num)  # for debuging purposes

while True:

    guess = int(input("Guess a number between 1 and 10: "))
    if guess == num:
        print("Correct!")
        break
    elif guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("Try again...")
