def cryptic_sorter(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda x: (len(x), x.lower(), x.swapcase()))
