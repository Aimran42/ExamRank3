def string_sculptor(text: str) -> str:
    result = []
    count = 0
    for c in text:
        if c.isalpha():
            result.append(c.lower() if count % 2 == 0 else c.upper())
            count += 1
        else:
            if c == ' ':
                count = 0
            result.append(c)
    return ''.join(result)
