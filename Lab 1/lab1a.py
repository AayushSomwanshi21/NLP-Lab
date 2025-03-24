import re

text = "Today's date is 24/02/2025, and the project started on 05/08/2023. Another important date is 31/12/2024."

dates = re.findall(
    r'\b(0[1-9]|[12][0-9]|[3][01])/(0[1-9]|1[0-2])/(\d{4})\b', text)

print(dates)
output = []

for date in dates:

    output.append('/'.join(date))

print(output)
