def cryptic_sorter(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda x: (len(x), x.lower(), x.swapcase()))

test1 = cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])

test2 = cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])

test3 = cryptic_sorter(["hello", "world", "hi", "test"])

test4 = cryptic_sorter([])

test5 = cryptic_sorter([""])


print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
