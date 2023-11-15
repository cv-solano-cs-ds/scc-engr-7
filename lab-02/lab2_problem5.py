"""
Computes all primes from 2 up to `upper_bound` provided in terminal by user.
"""

import sys


upper_bound = int(sys.argv[1])

# fill in your code for the above problem here
print("The following are prime:")

for n in range(2, upper_bound + 1):
    is_prime = True

    # We need only check for factors up to the square root of n.
    factor = 2
    while factor**2 <= n:
        if n % factor == 0:
            is_prime = False
            break
        factor += 1
    if is_prime:
        print(f"{n},", end=" ")
