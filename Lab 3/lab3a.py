# Generate prefixes and suffixes

import re

text = 'Hello'

n = len(text)

prefix = []
suffix = []

for i in range(1, n + 1):
    prefix.append(text[:i])

for i in range(n):
    suffix.append(text[i:])

print(f'Prefix: {prefix}\nSuffix: {suffix}')
