
# Functions useful to evaluate conversations

import tiktoken
import nltk
import numpy as np

# Strip GPT-4 related metadata from a conversation
def strip_gpt4_meta(conversation):
    # Strip some material from each line
    # Get rid of "{'role': 'user', 'content': "
    # Get rid of "{'role': 'assistant', 'content': "
    # Get rid of "}"
    # Remove extra whitespace
    # Remove first and last character
    no_meta = []
    for message_and_metadata in conversation:
        stripped = message_and_metadata.replace("{'role': 'user', 'content': ", "")
        stripped = stripped.replace("{'role': 'assistant', 'content': ", "")
        stripped = stripped.replace("}", "")
        stripped = stripped.strip()
        stripped = stripped[1:-1]
        no_meta.append(stripped)
    return no_meta

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
