
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0

    for char in s:
        if char.isalpha():  
            is_vowel = char in vowels
            is_consonant = not is_vowel

            if is_vowel:
                vowels_count += 1
            elif is_consonant:
                consonants_count += 1

    return vowels_count, consonants_count


input_string = input("Enter a string: ")


vowels, consonants = count_vowels_and_consonants(input_string)


print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")




