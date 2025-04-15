import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


def custom_tokenizer(text: str):

    text = text.lower()

    # Hashtags, mentions and links
    text = re.sub(r'#\w+|@\w+|http\S+|https\S+|www\S+', '', text)

    # Punctuations
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    tokens = word_tokenize(text)
    return tokens


text = 'Hey @john! Check out https://example.com #awesome #NLP. Running, runners, and runs are fun!'

tokens = custom_tokenizer(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print(f'Tokens: {tokens}')
for word in tokens:
    print(f'Lemmatizing: {lemmatizer.lemmatize(word)}')
    print(f'Stemming: {stemmer.stem(word)}')
