# Split at random point

import re
import random

text = 'Hello'

point = random.randint(0, len(text))

print(f'Split:{text[:point]} {text[point:]}')
