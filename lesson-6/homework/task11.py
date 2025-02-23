from collections import Counter
import string

def count_word_frequencies(filename='sample.txt', report_filename='word_count_report.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = text.split()
            word_counts = Counter(words)
            
            total_words = sum(word_counts.values())
            top_words = word_counts.most_common(5)
            
            print(f"Total words: {total_words}")
            print("Top 5 most common words:")
            for word, count in top_words:
                print(f"{word} - {count} times")
            
            with open(report_filename, 'w', encoding='utf-8') as report:
                report.write("Word Count Report\n")
                report.write(f"Total Words: {total_words}\n")
                report.write("Top 5 Words:\n")
                for word, count in top_words:
                    report.write(f"{word} - {count}\n")
                print(f"Word count report saved to {report_filename}")
    except FileNotFoundError:
        print("File 'sample.txt' not found. Please create it by typing a paragraph below.")
        user_text = input("Enter your text: ")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(user_text)
        print("File 'sample.txt' created. Now running word count analysis...")
        count_word_frequencies(filename, report_filename)

if __name__ == "__main__":
    count_word_frequencies()

