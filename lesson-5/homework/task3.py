def find_factors(n: int):
    """Prints the factors of a given positive integer."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

num = int(input("Enter a positive integer: "))

if num > 0:
    find_factors(num)
else:
    print("Please enter a positive integer.")