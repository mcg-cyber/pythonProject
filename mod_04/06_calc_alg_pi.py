import random

N = 1000000
n = 0

repeat = 0

while repeat < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    # print(x.y)
    repeat += 1

pii = 4 * n / N

print(pii)
