def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, otherwise returns False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
