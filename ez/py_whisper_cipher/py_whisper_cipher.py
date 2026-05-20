def whisper_cipher(text: str, shift: int) -> str:
    result = []
    for c in text:
        if c.isalpha():
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)
