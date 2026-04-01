def sum_of_harmonicSeries(num: int) -> float:
    sum_series = 0
    for i in range(1, num + 1):
        sum_series = sum_series + (1 / i)
    return f"{sum_series:.3f}"


print(sum_of_harmonicSeries(3))
print(sum_of_harmonicSeries(1))
print(sum_of_harmonicSeries(5))
print(sum_of_harmonicSeries(8))
