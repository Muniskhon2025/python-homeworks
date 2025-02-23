from collections import Counter
import string

def count_word_frequencies(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = text.split()
            word_counts = Counter(words)
            
            for word, count in word_counts.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    count_word_frequencies(filename)
