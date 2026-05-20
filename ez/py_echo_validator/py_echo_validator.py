def echo_validator(text: str) -> bool:
    if not text:
        return False
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]

# # ***dont push these test below***

# valid = 0
# if echo_validator("racecar"):
#     valid += 1
# if echo_validator("A man a plan a canal Panama"):
#     valid += 1
# if not echo_validator("race a car"):
#     valid += 1
# if echo_validator("Was it a car or a cat I saw"):
#     valid += 1
# if not echo_validator("hello"):
#     valid += 1
# if echo_validator("Madam Im Adam"):
#     valid += 1
# if not echo_validator(""):
#     valid += 1

# print(f"{valid}/7 tests passed")