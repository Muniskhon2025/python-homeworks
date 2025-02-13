
user_string = input("Enter a string: ")


start_word = input("Enter the word to check at the start: ")
end_word = input("Enter the word to check at the end: ")

if user_string.startswith(start_word) and user_string.endswith(end_word):
    print("The string starts with", start_word, "and ends with", end_word)
else:
    print("The string does not meet the criteria.")
