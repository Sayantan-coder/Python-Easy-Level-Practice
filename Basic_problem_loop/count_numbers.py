def count_number():
    Count = 0
    for num in range(1, 101):
        if num % 3 == 0:
            Count += 1
    return Count


Result = count_number()
print(Result)
