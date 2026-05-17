def cryptic_sorter(strings: list[str]) -> list[str]:
    strings.sort()
    ss = sorted(strings, key=lambda y: ord(y[0]) if y else 0)
    return sorted(ss, key=lambda x: (len(x), x.lower(), x.swapcase()))




from collections import deque

def rotateList(li: list, k: int) -> list:
    d = deque(li)
    d.rotate(k)
    return list(d)