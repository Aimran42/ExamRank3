def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# valid = 0
# if string_permutation_checker("abc", "bca") == True:
#     valid += 1
# if string_permutation_checker("abc", "def") == False:
#     valid += 1
# if string_permutation_checker("listen", "silent") == True:
#     valid += 1
# if string_permutation_checker("hello", "bello") == False:
#     valid += 1
# if string_permutation_checker("", "") == True:
#     valid += 1
# if string_permutation_checker("a", "") == False:
#     valid += 1
# if string_permutation_checker("Abc", "abc") == False:
#     valid += 1
# if string_permutation_checker("a gentleman", "elegant man") == True:
#     valid += 1

# print(f"{valid}/8 tests passed")