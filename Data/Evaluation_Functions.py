
# Functions useful to evaluate conversations

import tiktoken
import nltk
import numpy as np

# Get length using the tokenizer for the appropriate model
def get_length(string, model):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(string))

# Get nltk sentence length
def get_nltk_sentence_length(string):
    sentences = nltk.sent_tokenize(string)
    sen_lengths = []
    for sen in sentences:
        sen_lengths.append(len(nltk.word_tokenize(sen)))
    return np.mean(sen_lengths)
