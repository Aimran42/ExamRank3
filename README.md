<h2> In this exam you need to validate 6 exercices, each one of them gives you 16 point but the last one gives 20 point (aka 100/100 in total), and you will get randomly one of these 11 exercices below. GL in your exam ;D
<br><br>
<h2>1<br>
Write a function that checks if a string is a palindrome, ignoring spaces and case, only consider alphabetic characters for the comparison. The funct

Function signature
```python
def echo_validator(text: str) -> bool:
```


---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
echo_validator("racecar")
Output
True
Input
echo_validator("A man a plan a canal Panama")
Output
True
Input
echo_validator("race a car")
Output
False
Input
echo_validator("Was it a car or a cat I saw")
Output
True
Input
echo_validator("hello")
Output
False
Input
echo_validator("Madam Im Adam")
Output
True
Input
echo_validator("")
Output
False
```
<h2>2<br>
Write a function that mirrors a 2D matrix horizontally by reversing each row.

Function signature
```python
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
```



---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
mirror_matrix([[1, 2, 3], [4, 5, 6]])
Output
[[3, 2, 1], [6, 5, 4]]
Input
mirror_matrix([[1, 2], [3, 4], [5, 6]])
Output
[[2, 1], [4, 3], [6, 5]]
Input
mirror_matrix([[7]])
Output
[[7]]
Input
mirror_matrix([[1, 2, 3, 4]])
Output
[[4, 3, 2, 1]]
Input
mirror_matrix([[-1, -2], [-3, -4]])
Output
[[-2, -1], [-4, -3]]
```
<h2>3<br>
Write a function that merges two sorted lists into one sorted list.

Function signature
```python
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
```


---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
shadow_merge([1, 3, 5], [2, 4, 6])
Output
[1, 2, 3, 4, 5, 6]
Input
shadow_merge([1, 2, 3], [4, 5, 6])
Output
[1, 2, 3, 4, 5, 6]
Input
shadow_merge([1], [2, 3, 4])
Output
[1, 2, 3, 4]
Input
shadow_merge([], [1, 2, 3])
Output
[1, 2, 3]
Input
shadow_merge([1, 1, 2], [1, 3, 3])
Output
[1, 1, 1, 2, 3, 3]
```
<h2>4<br>
Write a function that creates a simple cipher by shifting letters in a st
by a given amount. Non-alphabetic characters should remain unchanged.

Function signature
```python
def whisper_cipher(text: str, shift: int) -> str:
```



---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
whisper_cipher("hello", 3)
Output
"khoor"
Input
whisper_cipher("Hello World!", 1)
Output
"Ifmmp Xpsme!"
Input
whisper_cipher("xyz", 3)
Output
"abc"
Input
whisper_cipher("ABC123def", 5)
Output
"FGH123ijk"
Input
whisper_cipher("", 10)
Output
""
```
<h2>5<br>
Write a function that sorts a list of strings according to multiple criteria:

1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.
Function signature
```python
def cryptic_sorter(strings: list[str]) -> list[str]:
```




---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])
Output
["cat", "dog", "apple", "banana", "elephant"]
Input
cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])
Output
["aaa", "AAA", "bbb", "BBB"]
Input
cryptic_sorter(["hello", "world", "hi", "test"])
Output
["hi", "test", "hello", "world"]
Input
cryptic_sorter([])
Output
[]
Input
cryptic_sorter([""])
Output
[""]
```
<h2>6<br>
Write a function that determines if two strings are permutations of each other.
Two strings are permutations if they contain the same characters with the same frequencies.
Function signature

```python
def string_permutation_checker(s1: str, s2: str) -> bool:
```



---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
string_permutation_checker("abc", "bca")
Output
True
Input
string_permutation_checker("abc", "def")
Output
False
Input
string_permutation_checker("listen", "silent")
Output
True
Input
string_permutation_checker("hello", "bello")
Output
False
Input
string_permutation_checker("", "")
Output
True
Input
string_permutation_checker("a", "")
Output
False
Input
string_permutation_checker("Abc", "abc")
Output
False
Input
string_permutation_checker("a gentleman", "elegant man")
Output
True
```

<h2>7<br>
Write a function that checks if brackets [], parentheses (), and braces {} are properly
balanced and correctly nested in a string. All others characters are ignored. Return True if balanced, False otherwise

Function signature
```python
def bracket_validator(s: str) -> bool:
```


---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
bracket_validator("()")
Output
True
Input
bracket_validator("()[]{}")
Output
True
Input
bracket_validator("(]")
Output
False
Input
bracket_validator("([)]")
Output
False
Input
bracket_validator("{[]}")
Output
True
Input
bracket_validator("hello(world)[test]{code}")
Output
True
Input
bracket_validator("((()))")
Output
True
Input
bracket_validator("((())")
Output
False
Input
bracket_validator("")
Output
True
```
<h2>8<br>
Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive, using digits 0-9 and letters A-Z for values 10-35. Return "ERROR" for invalid inputs (base, digits)

Function signature
```python
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
```


---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
number_base_converter("1010", 2, 10)
Output
"10"
Input
number_base_converter("FF", 16, 10)
Output
"255"
Input
number_base_converter("255", 10, 16)
Output
"FF"
Input
number_base_converter("123", 10, 2)
Output
"1111011"
Input
number_base_converter("Z", 36, 10)
Output
"35"
Input
number_base_converter("35", 10, 36)
Output
"Z"
Input
number_base_converter("123", 1, 10)
Output
"ERROR"
Input
number_base_converter("G", 16, 10)
Output
"ERROR"
```

<h2>9<br>
Write a function that counts the number of valid consecutive digit pairs in a
string. A valid pair consists of two adjacent digits where the second digit
is exactly one greater than the first digit. A 9 followed by a 0 is NOT a valid pair
and only consider consecutive characters that are both digits (0-9).
Function signature

```python
def pattern_tracker(text: str) -> int:
```
---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
pattern_tracker("123")
Output
2
Input
pattern_tracker("12a34")
Output
2
Input
pattern_tracker("987654321")
Output
0
Input
pattern_tracker("01234567")
Output
7
Input
pattern_tracker("abc")
Output
0
Input
pattern_tracker("1a2b3c4")
Output
0
Input
pattern_tracker("112233")
Output
2
```

<h2>10<br>
Write a function that transforms a string by alternating the case of alphabetic
characters only. Non-alphabetic characters remain unchanged and are ignored for
the purpose of alternation. The first alphabetic character should be lowercase,
the second uppercase, the third lowercase, and so on.
Function signature
   
```python
def string_sculptor(text: str) -> str:
```

---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
string_sculptor("hello")
Output
"hElLo"
Input
string_sculptor("Hello World")
Output
"hElLo wOrLd"
Input
string_sculptor("aBc123def")
Output
"aBc123DeF"
Input
string_sculptor("Python3.9!")
Output
"pYtHoN3.9!"
Input
string_sculptor("")
Output
""
```
<h2>11<br>
Write a function that rotates an array to the right by k positions, rotating right by k means the last k elements move to the front.
Function signature

```python
def twist_sequence(arr: list[int], k: int) -> list[int]:
```
---------------------------------------------------------------------------------------------------------------------------------------
```python Examples
Input
twist_sequence([1, 2, 3, 4, 5], 2)
Output
[4, 5, 1, 2, 3]
Input
twist_sequence([1, 2, 3], 1)
Output
[3, 1, 2]
Input
twist_sequence([1, 2, 3, 4], 0)
Output
[1, 2, 3, 4]
Input
twist_sequence([1, 2, 3], 5)
Output
[2, 3, 1]
Input
twist_sequence([], 3)
Output
[]
