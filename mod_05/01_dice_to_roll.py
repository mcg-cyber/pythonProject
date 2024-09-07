# This script asks the user amount of number to roll dice and then rolls the dice
#  finally prints all numbers

import random

"""
num_of_dice = int(input("Enter the number of dice you want to roll: "))
for _ in range(num_of_dice):
    total = random.randint(1, 6)
    print(total)
"""

#total = 0
num = int(input("Enter the number: "))
for _ in range(num):
    total = random.randint(1, 6)
    #total += num
    print(total)


