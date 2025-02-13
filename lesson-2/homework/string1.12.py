words = input("Enter a list of words separated by spaces: ").split()
separator = input("Enter the separator character (e.g., '-', ','): ")

joined_string = separator.join(words)

print("Joined string:", joined_string)
