import re
import spacy
import nltk
from nltk.tokenize import word_tokenize
from spacy import displacy


def normalize(text: str):

    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    # NER
    print('NER:')
    for ent in doc.ents:
        print(f'{ent.text}: {ent.label_}')

    # POS Tagging
    print('\nPOS Tags:')
    for word in doc:
        print(f'{word}: {word.pos_}')

    # Noun Phrase
    print('\nNoun Phrases:')
    for word in doc.noun_chunks:
        print(word.text)

    # Syntactic Structure
    for sent in doc.sents:
        for token in sent:
            if token.dep_ in ('nsubj', 'dobj'):
                print(f'{token.dep_}: {token.text} (Head: {token.head.text})')

    displacy.serve(doc, style='dep')


text = 'Elon Musk owns Tesla and is a billionaire'
normalize(text)
