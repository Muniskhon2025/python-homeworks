


user_string = input("Enter a string: ")

vowels = ('a', 'e', 'i', 'o', 'u')

for vowel in vowels:
    user_string = user_string.replace(vowel, "*")


print("Modified string:", user_string)
