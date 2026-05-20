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

# dont push these test below

# valid = 0
# if whisper_cipher("hello", 3) == "khoor":
#     valid += 1
# if whisper_cipher("Hello World!", 1) == "Ifmmp Xpsme!":
#     valid += 1
# if whisper_cipher("xyz", 3) == "abc":
#     valid += 1
# if whisper_cipher("ABC123def", 5) == "FGH123ijk":
#     valid += 1
# if whisper_cipher("", 10) == "":
#     valid += 1

# print(f"{valid}/5 tests passed")