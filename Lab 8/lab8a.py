import re


slangs = {
    'brb': 'be right back',
    'omg': 'Oh my god',
    'rn': 'right now',
    'lmao': 'laughing my ass off'
}


def clean(text: str):

    normalised_word = []

    text.lower()
    text = re.sub(r'[\U0001F600-\U0001F64F]', '', text)
    words = text.split()

    for word in words:
        normalised_word.append(slangs.get(word, word))

    normalised_text = ' '.join(normalised_word)
    normalised_text = re.sub(r'([!?.,]){1,}', r'\1', normalised_text)
    normalised_text = re.sub(r'\s{1,}', ' ', normalised_text)

    return normalised_text


text = "omg!!!  u r so funny 😂😂😂"

print(clean(text))
