def one_word(text):
    """
    Detects if the text consists of only one word.

    Parameters:
    text (str): The input text to check.

    Returns:
    bool: True if there is only one word, False otherwise.
    """
    return len(text.split()) == 1
