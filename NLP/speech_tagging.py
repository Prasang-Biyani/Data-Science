import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_txt = state_union.raw("2005-GWBush.txt")
sample_txt = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_txt)
tokenized = custom_sent_tokenizer.tokenize(sample_txt)
# print(tokenized)
def process_content() -> None:
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tag = nltk.pos_tag(words)
            print(tag)
    except Exception as e:
        print(e)

process_content()