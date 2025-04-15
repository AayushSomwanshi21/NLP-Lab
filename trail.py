import re

text = "Contact me at abc.mahe@manipal.edu before 12/04/2025"

tokens = text.split()
cur = ''

output = []
for token in tokens:

    if re.search(r'([a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z0-9._]{2,})', token) or re.search(r'(0[1-9]|[12][0-9]|3[10])/(0[1-9]|1[0-2])/(\d{4})', token):
        output.append(cur.strip())
        cur = ''
        output.append(token)
    else:
        cur = cur + token + ' '

print(output)
