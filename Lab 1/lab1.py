import re

text = "This is a sample text,with some punctuation marks! Also, newlines and  carriage returns.Let's split it."

output = re.findall(r'\b\w+\b', text)
print(output)
