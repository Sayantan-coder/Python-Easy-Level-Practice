def is_curzon(num: int) -> bool:
    a = 2**num + 1
    b = 2 * num + 1
    if a % b == 0:
        return True
    return False


Result = is_curzon(5)
print(Result)
