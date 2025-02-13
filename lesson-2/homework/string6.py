def get_last_digit(number):
    return abs(number) % 10  # Gets the last digit of any number

# Get user input
num = int(input("Enter a number: "))

# Print the last digit
print("The last digit of", num, "is", get_last_digit(num))


