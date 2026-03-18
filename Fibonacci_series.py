def FibonaciSeries(num: int):
    prev = 0
    curr = 1
    for i in range(1, num + 1):
        print(prev)
        next = prev + curr
        prev = curr
        curr = next


FibonaciSeries(10)
