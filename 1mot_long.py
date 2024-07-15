def word_too_long(text):
    """
    Detects if any word in the text is longer than 13 characters.

    Parameters:
    text (str): The input text to check.

    Returns:
    bool: True if any word is too long, False otherwise.
    """
    return any(len(word) > 13 for word in text.split())
