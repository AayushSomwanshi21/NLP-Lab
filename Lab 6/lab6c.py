# Extract all formats of date

import re

text = "Today's date is 25/03/2025. Yesterday was 03-25-2025 and tommorow's date will be March 25,2025"

output = re.findall(
    r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b', text)

output1 = re.findall(
    r'\b(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})\b', text)

output2 = re.findall(
    r'\b(Jan|Feb|March|April|May|June|July|August|Sept|Oct|Nov|Dec) (\d{1,2}),(\d{4})\b', text)

print(output, output1, output2)
