def get_sum(num: int) -> int:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


result = get_sum(12)
print(result)
