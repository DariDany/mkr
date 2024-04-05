from collections import Counter
import re

def find_popular_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text.lower())
            word_counts = Counter(words)
            popular_words = word_counts.most_common(10)
            popular_words_dict = dict(popular_words)
            return popular_words_dict
    except FileNotFoundError:
        print("File not found.")
        return {}

def main(file_name):
    res = find_popular_words(file_name)
    for word, count in res.items():
        print(f"{word}-{count}\n")

if __name__ == '__main__':
    main('input.txt')