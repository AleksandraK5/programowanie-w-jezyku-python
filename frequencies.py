import string
from collections import Counter


def word_frequencies(text: str) -> dict:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    return dict(Counter(text))
