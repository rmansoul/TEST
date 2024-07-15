import re

# Arabic phrases
arabic_phrases = [
    "ريدا ريدا ريدا انتقلت",
    "ريدا انتقلت ريدا انتقلت",
    "ريدا انتقلت إلى باريس إلى باريس"
]

# Regular expression to detect repetitions of phrases more than twice consecutively
repetition_phrase_regex = r'\b(\S+(\s+\S+)*)\s+\1\b'

# Check each phrase
for phrase in arabic_phrases:
    repetitions_phrase = re.findall(repetition_phrase_regex, phrase)
    if repetitions_phrase:
        print(f"Repetitions of phrases detected in Arabic in '{phrase}' : {repetitions_phrase}")
    else:
        print(f"No repetitions of phrases detected in Arabic in '{phrase}'.")
