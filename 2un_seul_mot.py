import re

# Phrase in Arabic
arabic_phrase = "ريدا"

# Regular expression to check for a single word in Arabic
single_word_regex = r'^\b[\u0600-\u06FF]+\b$'

# Check if the phrase contains a single word
if re.match(single_word_regex, arabic_phrase):
    print(f"The phrase '{arabic_phrase}' contains a single word in Arabic.")
else:
    print(f"The phrase '{arabic_phrase}' does not contain a single word in Arabic.")
