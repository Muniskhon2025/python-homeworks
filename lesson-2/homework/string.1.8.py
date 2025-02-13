str = input('Enter a word: ')

if len(str) > 0:
    # Print first and last characters
    first_char = str[0]
    last_char = str[-1]
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
else:
    print("The string is empty.")


#Alternative
    str = input('Enter a word: ')

print(str[0])
print(str[-1])