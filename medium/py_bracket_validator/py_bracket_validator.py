def bracket_validator(s: str) -> bool:
    lst = []

    pairs = {'}':'{',']':'[', ')':'('}
    for c in s:
        if c in '{[(':
            lst.append(c)
        elif c in '}])':
            if not lst or lst[-1] != pairs[c]:
                return False
            lst.pop()
    return not lst

# do not push this test below

# valid = 0
# if bracket_validator("()") == True:
#     valid += 1
# if bracket_validator("()[]{}") == True:
#     valid += 1
# if bracket_validator("(]") == False:
#     valid += 1
# if bracket_validator("([)]") == False:
#     valid += 1
# if bracket_validator("{[]}") == True:
#     valid += 1
# if bracket_validator("hello(world)[test]{code}") == True:
#     valid += 1
# if bracket_validator("((()))") == True:
#     valid += 1
# if bracket_validator("((())") == False:
#     valid += 1
# if bracket_validator("") == True:
#     valid += 1

# print(f"{valid}/9 tests passed")