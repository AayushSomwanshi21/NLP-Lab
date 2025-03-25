# Remove digits from sentence using Greedy tokenizer
# Additional Q1,Q2

import re
import nltk

text = "Hello, I have 2 apples and 3 bananas."

tokens = text.split()
output = []
count = 0
digits = []

for token in tokens:

    if not re.search(r'\d', token):
        output.append(token)
    else:
        count += 1
        digits.append(token)


print(' '.join(output))
print(f'Digits: {digits} Number of digits: {count}')
