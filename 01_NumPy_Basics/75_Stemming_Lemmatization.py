import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ["rocks", "corpora", "better", "running"]
# 'better' ko ye 'good' mein convert kar dega
lemmatized_words = [lemmatizer.lemmatize(w, pos="v") for w in words]

print(f"Original: {words}")
print(f"Lemmatized: {lemmatized_words}")
