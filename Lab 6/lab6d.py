# Extract all kinds of date and standardize them to a common format

import re

text = 'Call me at 123-456-7890 or (123) 456-7890. Also, my international numbers are +1 987-654-3210 and +91 98765 43210. You can also reach me at 123.456.7890 or 123 456 7890.'

dates = re.findall(
    r'\+\d{1,2} \d{5} \d{5}|(?:\+\d{1,2})? \(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}', text)

print(dates)

n = len(dates)

for i in range(n):

    dates[i] = re.sub(r'[\s.()-]', '', dates[i])

print(dates)

common_format = []

for date in dates:

    if date.startswith('+') and len(date) == 13:
        date = date[:3] + ' ' + date[3:8] + ' ' + date[8:]

    elif date.startswith('+') and len(date) == 12:
        date = date[:2] + ' ' + date[2:7] + ' ' + date[7:]

    else:
        date = '+1' + ' ' + date[:5] + ' ' + date[5:]

    common_format.append(date)

print(common_format)
