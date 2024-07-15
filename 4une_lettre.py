import re

# Given phrase
phrase = "a b c و d e f g و"

# Regular expression to detect a single letter, excluding "و"
single_letter_regex = r'\b(?![و])\w\b'

# Search for words with a single letter, excluding "و"
words_single_letter = re.findall(single_letter_regex, phrase)

# Display the found words
if words_single_letter:
    print(f"Words with a single letter, excluding 'و': {words_single_letter}")
else:
    print("No words with a single letter, excluding 'و', found in the phrase.")
