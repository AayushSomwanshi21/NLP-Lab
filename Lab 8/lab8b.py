import re

slangs = {
    'brb': 'be right back',
    'omg': 'Oh my god',
    'rn': 'right now',
    'u': 'you'
}


def normalize(text: str):

    text = text.lower()

    text = re.sub(r'[\U0001F600-\U0001F64F]', '', text)
    tokens = text.split()

    normalized_word = []

    for word in tokens:
        normalized_word.append(slangs.get(word, word))

    text = ' '.join(normalized_word)

    text = re.sub(r'([!?.,;]){1,}', r'\1', text)

    return text


text = 'OMG !!! you,,, Are so funny 😂😂'
print(normalize(text))
