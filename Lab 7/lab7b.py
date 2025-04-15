import re
import spacy


nlp = spacy.load('en_core_web_sm')

text = 'John Doe paid $5000 to Microsoft on January 5, 2022. He will pay another $3000  on 12/04/2025.'

doc = nlp(text)

for ent in doc.ents:
    print(f'{ent.text}->{ent.label_}')

normalized_tokens = []

for token in doc:

    if token.like_num:
        normalized_tokens.append('<NUMBER>')

    elif token.ent_type_ == 'DATE':
        normalized_tokens.append('<DATE>')

    elif token.ent_type_ == 'MONEY':
        normalized_tokens.append('<MONEY>')
    else:
        normalized_tokens.append(token.text)

print(' '.join(normalized_tokens))
