def is_prime(num) -> bool:
    if num == 1:
        print("Neither Prime nor not Prime")
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


result = is_prime(1)
print(result)
