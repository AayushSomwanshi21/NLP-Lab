# Count non alphanumeric characters

import re

count = 0

text = '!Hello, World!!'

for char in text:

    if re.match(r'[^a-zA-Z0-9]', char):
        count += 1

print(count)
