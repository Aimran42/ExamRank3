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
