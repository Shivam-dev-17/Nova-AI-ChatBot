import re

def clean_text(text):
    text = text.lower()
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    return text

def tokenize(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    return words
