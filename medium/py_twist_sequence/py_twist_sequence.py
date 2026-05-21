def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr
