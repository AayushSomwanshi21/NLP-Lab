# Split a word into pairs at all possible positions

import re

text = 'Hello'

output = []

for i in range(1, len(text)):
    output.append((text[:i], text[i:]))

print(output)
