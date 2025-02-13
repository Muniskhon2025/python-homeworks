sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")

new_sentence = sentence.replace(word_to_replace, replacement_word)
print("Updated sentence:", new_sentence)