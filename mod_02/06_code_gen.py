__author__ = '<Cahit Gunes>'
__email__ = '<cahit.gunes@metropolia.fi>'

import random

def generate_code():
    nums = []
    for _ in range(4):
        nums += int(random.randint(1, 6))
    print(nums)

print("First code:")
generate_code()

print("Second code:")
generate_code()