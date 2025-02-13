str = input("Enter a word: ")

if str == str[::-1]:
    print(f"{str} is a plaindrome.")
else:
    print(f"{str} is not a plaindrome.")