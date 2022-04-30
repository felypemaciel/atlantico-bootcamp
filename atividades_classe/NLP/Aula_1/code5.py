import matplotlib.pyplot as plt
import re
from nltk.tokenize import regexp_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal
import numpy as np

# Split the script into lines: lines
holy_grail = get_sample_Santo_Graal()
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', lines) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(lines,"\w+") for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [np.length(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()