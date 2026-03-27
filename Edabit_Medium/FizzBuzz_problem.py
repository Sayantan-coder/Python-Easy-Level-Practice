def FizzBuzz(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print(FizzBuzz(45))
print(FizzBuzz(25))
print(FizzBuzz(37))
print(FizzBuzz(9))
