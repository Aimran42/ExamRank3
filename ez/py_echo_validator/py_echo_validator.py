def echo_validator(text: str) -> bool:
    if not text:
        return False
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]
