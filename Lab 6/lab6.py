# Remove noise from text

import re

text = "This is a #sample text! Remove the #hashtag and noise! Visit @example."

output = re.sub(r'[^a-zA-Z0-9\s]', '', text)

print(output)
