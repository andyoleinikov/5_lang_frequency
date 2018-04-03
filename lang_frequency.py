import sys
import os
import re
import heapq
from collections import Counter


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as text_file:
            return text_file.read()
    return None


def get_most_frequent_words(text):
    sliced_text = [word.lower() for word in re.split('\W+', text) if word]
    words_with_frequences = dict(Counter(sliced_text))
    most_frequent_words = heapq.nlargest(
        10,
        words_with_frequences,
        key=words_with_frequences.__getitem__
    )
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')

    filepath = sys.argv[1]
    text_from_file = load_data(filepath)
    most_frequent_words = get_most_frequent_words(text_from_file)

    if most_frequent_words == []:
        sys.exit('Empty file')
        
    print('Ten most frequent words: {}'.format(', '.join(most_frequent_words)))
