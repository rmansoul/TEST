import re

# Arabic string
arabic_words = "منسول منسسس"

# Regular expression to detect three identical consecutive letters
three_identical_letters_regex = r'\b\w*(\w)\1{2}\w*\b'

# Search for words with three identical consecutive letters
words_with_three_identical_letters = re.findall(three_identical_letters_regex, arabic_words)

# Display the found words
if words_with_three_identical_letters:
    print(f"Words with three identical consecutive letters in Arabic: {words_with_three_identical_letters}")
else:
    print("No words with three identical consecutive letters found in the Arabic string.")
