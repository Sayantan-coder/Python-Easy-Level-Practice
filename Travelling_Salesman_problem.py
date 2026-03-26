def path(num: int) -> int:
    total_path = 1
    for value in range(1, num + 1):
        total_path *= value
    return total_path


print(path(4))
print(path(1))
print(path(9))
