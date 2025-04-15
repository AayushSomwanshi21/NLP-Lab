import re
import nltk
from nltk.tokenize import word_tokenize

text = 'The book is kept on the table'

tokens = word_tokenize(text)

tags = nltk.pos_tag(tokens)

for word, tag in tags:
    print(f'{word}: {tag}')
