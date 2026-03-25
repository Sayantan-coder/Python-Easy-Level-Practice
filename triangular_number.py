def triangular_pattern(num: int) -> int:
    result = 0
    for i in range(num + 1):
        result += i
    return result


print(triangular_pattern(6))
