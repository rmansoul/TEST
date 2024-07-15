import re

# Phrase in Arabic
arabic_phrase = "رائعة جدا ومثيرة للدهشة جداممممممممممم جدا جدا"

# Regular expression to detect a word with more than 13 letters
long_arabic_word_regex = r'\b\w{14,}\b'

# Search for words with more than 13 letters in the Arabic phrase
long_arabic_words = re.findall(long_arabic_word_regex, arabic_phrase)

# Display the found words
if long_arabic_words:
    print(f"Words with more than 13 letters found in Arabic: {long_arabic_words}")
else:
    print("No word with more than 13 letters found in the Arabic phrase.")
