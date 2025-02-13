user_string = input("Enter a string: ")

if any(char.isdigit() for char in user_string):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")
