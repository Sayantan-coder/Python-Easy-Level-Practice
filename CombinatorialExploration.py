def no_permutation_digits(num: int) -> int:
    count = 0
    permutation = 1
    for number in range(1, num + 1):
        permutation *= number
    while permutation:
        digit = permutation % 10
        count += 1
        permutation = permutation // 10
    return count


print(no_permutation_digits(1))
print(no_permutation_digits(3))
print(no_permutation_digits(5))
print(no_permutation_digits(8))
