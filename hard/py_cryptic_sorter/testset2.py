from collections import deque

def rotateList(li: list, k: int) -> list:
    d = deque(li)
    d.rotate(k)
    return list(d)


def cryptic_sorter(strings: list[str]) -> list[str]:
    ss = strings.sort()
    return sorted(ss, key=lambda x: (len(x)))