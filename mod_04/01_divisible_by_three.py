# This script prints all numbers which is devisble by 3 in range 1-1000
# Uncomment break to stop the loop!

import random

while True:
    number_range = random.randint(1, 1000)
    if number_range % 3 == 0:
        print(number_range)
        # break
