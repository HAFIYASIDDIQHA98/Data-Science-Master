import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# NLTK resources download karein (pehli baar ke liye)
nltk.download('punkt')

text = "Hafiya is a software engineer. She is learning NLP today."

sentences = sent_tokenize(text)
words = word_tokenize(text)

print("Sentences:", sentences)
print("Words:", words)
