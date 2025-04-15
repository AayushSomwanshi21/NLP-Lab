import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
text = 'He was running so fast that he collided on the wall'

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
tokens = word_tokenize(text)

print("The tokens are: ", tokens)
for word in tokens:
    print(f'Stemmed Word: {stemmer.stem(word)}')
    print(f'Lemmatized Word: {lemmatizer.lemmatize(word)}')
