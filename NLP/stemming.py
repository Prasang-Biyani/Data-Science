from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ['python', 'python', 'pythoning', 'pythoned', 'pythonly']

for w in example_words:
    print(ps.stem(w))

new_txt = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_txt)
for w in words:
    print(ps.stem(w))
