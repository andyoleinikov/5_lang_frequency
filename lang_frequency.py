import sys
import os
import re
from collections import Counter


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as text_file:
            return text_file.read()
    return None


def get_most_frequent_words(text):
    sliced_text = re.findall(r'\w+', text.lower())
    most_frequent_words = [
        word[0] for word in Counter(sliced_text).most_common(10)
    ]
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')

    filepath = sys.argv[1]
    text_from_file = load_data(filepath)
    most_frequent_words = get_most_frequent_words(text_from_file)

    if not most_frequent_words:
        sys.exit('Empty file')

    print(
        'Ten most frequent words in descending order:\n{}'
        .format(', '.join(most_frequent_words))
    )
