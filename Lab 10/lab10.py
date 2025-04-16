import nltk
from nltk.tag import hmm
from nltk.tokenize import word_tokenize

# Prepare sequences of tagged words per sentence (even if it's just one word each for now)
train_data = {
    'Finance': ['stock market crashed', 'economic growth'],
    'Sports': ['tennis tournament', 'football match cricket world cup', 'sports event'],
}

# Convert to sequence of tagged words for each sentence
tagged_sequences = []
for label, phrases in train_data.items():
    for phrase in phrases:
        tokens = word_tokenize(phrase.lower())
        tagged_sequences.append([(word, label) for word in tokens])
print(tagged_sequences)
# Train HMM model
trainer = hmm.HiddenMarkovModelTrainer()
model = trainer.train(tagged_sequences)

# Prediction function


def predict(text: str):
    words = word_tokenize(text.lower())
    tagged_sentence = model.tag(words)
    tags = [tag for _, tag in tagged_sentence]
    print(tags)
    return max(set(tags), key=tags.count) if tags else 'Unknown'


# Testing
test_data = {
    'Finance': 'The stock market is down',
    'Sports': 'The football match was good',
}

true_labels = list(test_data.keys())
pred_labels = [predict(sentence) for sentence in test_data.values()]

print('Predicted:', pred_labels)
