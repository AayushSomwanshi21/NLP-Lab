from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from hmmlearn.hmm import GaussianHMM
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB

data = fetch_20newsgroups(categories=['comp.graphics', 'sci.med'], remove=(
    'headers', 'footers', 'quotes'))

labels = [0 if target == 0 else 1 for target in data.target]

vectorize = CountVectorizer()
x = vectorize.fit_transform(data.data).toarray()

model = GaussianHMM(n_components=3, covariance_type='diag', n_iter=100)
model.fit(x)

features = model.predict(x).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(f'Accuracy Score: {accuracy_score(y_true=y_test, y_pred=y_pred)}')
