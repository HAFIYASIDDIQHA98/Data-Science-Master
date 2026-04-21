from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')

text = "This is a very simple example to show how stopwords work."
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)

# Stopwords ko filter karna
filtered_text = [w for w in words if w.lower() not in stop_words]

print("Original Words:", words)
print("After Removing Stopwords:", filtered_text)
