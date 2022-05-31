import math


def is_prime(n: int) -> bool:
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

    # A little optimization
    for i in range(2, math.sqrt(n)):
        if n % i == 0:
            return False
    return True
