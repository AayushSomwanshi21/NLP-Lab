# Replace all non alphanumeric characters with a given character

import re

text = '!Hello, World!!'

char = '$'

output = re.sub(r'[^a-zA-Z0-9]', char, text)

print(output)
