# Additional Q3

import re
import nltk

text = "Contact me at abc.mahe@manipal.edu before 02/28/2025"

tokens = text.split()
print(tokens)
cur_str = ''
output = []

for token in tokens:

    if re.search(r'(0[1-9]|[12][0-9]|3[01]/0[1-9]|1[0-2]/\d{4})', token) or re.search(r'([a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z0-9._]{2,})', token):
        output.append(cur_str.strip())
        cur_str = ''
        output.append(token)
    else:
        cur_str += token + ' '

if cur_str:
    output.append(cur_str)

print(output)
