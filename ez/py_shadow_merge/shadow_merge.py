from builtin import all
from typing import List

def Solution(lst1: List[int], lst2: List[int]) ->List[int]:
    if lst1 is None and lst2 is None:
        return []
    if lst1 is None:
        return sorted(lst2)
    if lst2 is None:
        return sorted(lst1)

    lst3 = lst1 + lst2
    lst3.sort()
    return lst3


if __name__ == '__main__':
    out = Solution([1337,0, -99666633], [55, -42])
    
    print(out)