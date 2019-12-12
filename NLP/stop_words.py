from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "There are a number of myths and legends associated with the origin of the name Delhi. One of them is derived from Dhillu or Dilu, a king who built a city at this location in 50 BCE and named it after himself"
stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sentence)
# filtered_sentence = []
# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
# print(filtered_sentence)

filtered_sentence = [w for w in words if w not in stop_words]
print(filtered_sentence)