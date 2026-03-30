def count_solution(a: int, b: int, c: int) -> int:
    value = (b * b) - (4 * a * c)
    if value > 0:
        return 2
    elif value == 0:
        return 1
    else:
        return ValueError("No real solution exit")


print(count_solution(1, 0, -1))
print(count_solution(4, -6, 3))
print(count_solution(1, 0, 0))
print(count_solution(1, 0, 1))
