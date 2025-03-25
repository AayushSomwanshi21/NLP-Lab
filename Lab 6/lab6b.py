# Remove extra whitespace from text

import re

text = 'This   is a sentence with   extra whitespace  '

output = re.sub(r'\s{1,}', ' ', text)

print(output)
