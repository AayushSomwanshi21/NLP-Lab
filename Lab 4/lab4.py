# Frequency of N-Grams
# Additional Q1,Q2

import nltk
from nltk.util import ngrams
from collections import Counter

nltk.download('punkt_tab')


def count_ngrams_freq(text: str, reversed_text: str, n: int):

    tokens = nltk.word_tokenize(text.lower())
    reversed_tokens = nltk.word_tokenize(reversed_text.lower())

    n_grams = ngrams(tokens, n)
    n_grams_reversed = ngrams(reversed_tokens, n)

    n_grams = list(n_grams)
    n_grams_reversed = list(n_grams_reversed)

    freq = Counter(n_grams)
    freq1 = Counter(n_grams_reversed)

    total = len(n_grams)

    prob = {gram: round(count/total, 2) for gram, count in freq.items()}

    return freq, freq1, prob


text = 'This is a sample text and this is also a sample text'

words = text.split()
words = words[::-1]

reversed_text = ' '.join(words)
print(reversed_text)

n = 2
freq, freq1, prob = count_ngrams_freq(text, reversed_text, n)

print('Frequency:\n', freq)
print('Reversed Frequency:\n', freq1)
print('Probability:\n', prob)
