# Remove digits from sentence using Greedy tokenizer

import re
import nltk

text = "Hello, I have 2 apples and 3 bananas."

tokens = text.split()
output = []

for token in tokens:

    if not re.search(r'\d', token):
        output.append(token)

print(' '.join(output))
