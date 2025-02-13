
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

import datetime
current_year = datetime.datetime.now().year


age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")
