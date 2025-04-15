import re

slangs = {
    'brb': 'be right back',
    'omg': 'Oh my god',
    'rn': 'right now',
    'lmao': 'laughing my ass off'
}

text = 'omg thats so cool lmao. I will brb'
text = text.split()
result = []
for word in text:

    word = slangs.get(word, word)
    result.append(word)

print(result)
