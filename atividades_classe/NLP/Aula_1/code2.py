# Import necessary modules
import os
import sys
sys.path.append(os.getcwd().split('/NLP')[0])
from nltk.tokenize import word_tokenize, sent_tokenize
from nlp_utils import get_sample_Santo_Graal

# Split scene_one into sentences: sentences
scene_one = get_sample_Santo_Graal()
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(sentences)

# Print the unique tokens result
print(unique_tokens)
