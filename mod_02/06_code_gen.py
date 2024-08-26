# Scripts prints  4 digits etween 1-6 twicw using random module

import random


def generate_code():
    nums = []
    for _ in range(4):
        nums.append(random.randint(1, 6))
    print(nums)


print("First code:")
generate_code()

print("Second code:")
generate_code()
