from math import gcd
from random import randint


def is_prime(n: int, k=3):
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True

    # Try k times
    for _ in range(k):
        a = randint(2, n-2)
        # Fermat's little theorem
        if pow(a, n - 1) % n != 1:
            return False
    return True


