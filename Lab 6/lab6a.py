# Remove emojis from text

import re

text = 'Hello, that was very funny😂😂😂😂'

output = re.sub(r'[\U0001F600-\U0001F64F]', '', text)

print(output)
