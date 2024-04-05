from collections import Counter
import re

def find_popular_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        popular_words = word_counts.most_common(10)
        return popular_words
