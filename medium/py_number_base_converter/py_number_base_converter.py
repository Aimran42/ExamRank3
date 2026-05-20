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
