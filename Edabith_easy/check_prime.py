def is_prime(num) -> bool:
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num - 1):
            if num % i == 0:
                return False
        return True


result = is_prime(-4)
print(result)
