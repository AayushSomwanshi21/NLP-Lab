# Remove non alphanumeric characters from start and end of the string

import re

text = "!Hello, World?!"

output = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', text)

print(output)
