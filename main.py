from collections import Counter
import re

def find_popular_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text.lower())
            word_counts = Counter(words)
            popular_words = word_counts.most_common(10)
            return popular_words
    except FileNotFoundError:
        print("File not found.")
        return []

def write_most_common_words(file_name, popular_words):
    try:
        with open(file_name, 'w') as file:
            for word, count in popular_words:
                file.write(f"{word}-{count}\n")
        print("Results written to", file_name)
    except IOError:
        print("Error writing to file.")
