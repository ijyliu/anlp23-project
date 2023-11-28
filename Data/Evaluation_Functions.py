
# Functions useful to evaluate conversations

import re
import nltk
import numpy as np
from unidecode import unidecode

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

# Cleanup for CW compliance
# Strip GPT-4 related metadata from a conversation
# DO NOT remove extra whitespace in this version
def gpt4_cw_cleanup(conversation):
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
        # Replace any number of spaces and then a newline with a newline
        stripped = re.sub(r'\s+\n', '\n', stripped)
        # Remove all \r
        stripped = stripped.replace("\r", "")
        stripped = stripped.replace("\\r", "")
        # Replace ".  \n" with ".\n"
        stripped = stripped.replace(".  \\n", ".\\n")
        # Replace ". \n" with ".\n"
        stripped = stripped.replace(". \n", ".\n")
        # Replace any number of spaces and then literal \n with literal \n
        #stripped = re.sub(r' \\n', '\\n', stripped)
        # Convert to ascii
        stripped = unidecode(stripped)
        #stripped = stripped.strip()
        stripped = stripped[1:-1]
        # Strip newlines or spaces at the very end of the string
        stripped = re.sub(r'[\s\n]+$', '', stripped)
        # If last character is a newline, remove it
        if stripped[-1] == '\n':
            stripped = stripped[:-1]
        # If last character is literal "\n", remove it
        if stripped[-2:] == '\\n':
            stripped = stripped[:-2]
        # Replace "\'" with "'"
        stripped = stripped.replace("\\'", "'")
        no_meta.append(stripped)
    return no_meta

# Text-davinci-003 cleanup
def td3_cw_cleanup(conversation):
    cleaned_up = []
    for message in conversation:
        # Remove any number of spaces and then a newline
        new_message = re.sub(r'\s+\n', '\n', message)
        # Convert to ascii
        new_message = unidecode(new_message)
        cleaned_up.append(new_message)
    return cleaned_up

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
