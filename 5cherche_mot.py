import re

# Arabic string
chaine = "ريدا هو بعيد جدا عن هنا"

# Arabic words to search for
word_search1 = "ريدا"
word_search2 = "هو"

# Regular expression to search for exact words
expression_regex = r'\b(?:' + re.escape(word_search1) + r'|' + re.escape(word_search2) + r')\b'

# Search for exact words in the string
for match in re.finditer(expression_regex, chaine):
    word_find = match.group()
    indice_debut = match.start()
    print(f"The word '{word_find}' was found in the string at index {indice_debut}.")
