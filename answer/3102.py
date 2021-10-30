import math

m = int(input())

for i in range(2, m + 1):
    is_prime = True
    for div in range(2, int(math.sqrt(i)) + 1):
        if not i % div:
            is_prime = False
            break
    if is_prime:
        print("{} is prime".format(i))
