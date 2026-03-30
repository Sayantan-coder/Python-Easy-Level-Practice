def right_shift(x: int, y: int) -> int:
    result = x // 2**y
    return result


print(right_shift(80, 3))
print(right_shift(-24, 2))
print(right_shift(-5, 1))
print(right_shift(100, 6))
