def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        decimal = int(number, from_base)
    except:
        return "ERROR"

    if to_base == 10:
        return str(decimal)
    
    result = ""
    while decimal:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result or "0"

valid = 0
if number_base_converter("1010", 2, 10) == "10":
    valid += 1
if number_base_converter("FF", 16, 10) == "255":
    valid += 1
if number_base_converter("255", 10, 16) == "FF":
    valid += 1
if number_base_converter("123", 10, 2) == "1111011":
    valid += 1
if number_base_converter("Z", 36, 10) == "35":
    valid += 1
if number_base_converter("35", 10, 36) == "Z":
    valid += 1
if number_base_converter("123", 1, 10) == "ERROR":
    valid += 1
if number_base_converter("G", 16, 10) == "ERROR":
    valid += 1

print(f"{valid}/8 tests passed")