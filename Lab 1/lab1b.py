import re

text = 'Call me at 123-456-7890 or (123) 456-7890. Also, my international numbers are +1 987-654-3210 and +91 98765 43210. You can also reach me at 123.456.7890 or 123 456 7890.'

output = re.findall(
    r'\+\d{1,2} \d{5} \d{5}|(?:\+\d{1,2})?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}', text)
print(output)


# r'\+\d{1,2} \d{5} \d{5}|(?:\+\d{1,2}[ -])?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}'
