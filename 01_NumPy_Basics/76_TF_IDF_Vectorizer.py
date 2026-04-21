from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'Python is great for coding.',
    'Coding in Python is fun.',
    'Hafiya likes Python coding.'
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print("Feature Names:", vectorizer.get_feature_names_out())
print("TF-IDF Matrix:\n", X.toarray())
