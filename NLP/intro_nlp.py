from nltk.tokenize import sent_tokenize, word_tokenize
sample_text = 'The first serious and documented attempts to organize civil engineers as a professional society in the newly created United States were in the early 19th century.'

# print(sent_tokenize(sample_text))
# print(word_tokenize(sample_text))

for i in word_tokenize(sample_text):
    print(i)

