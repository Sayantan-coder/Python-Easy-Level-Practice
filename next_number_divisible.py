def divisible_by_b(a: int, b: int) -> int:
    if a % b == 0:
        num = a + 1
        while num % b != 0:
            num += 1
        return num
    else:
        while a % b != 0:
            a += 1
        return a


print(divisible_by_b(18, 6))
print(divisible_by_b(17, 5))
print(divisible_by_b(98, 9))
print(divisible_by_b(14, 11))
