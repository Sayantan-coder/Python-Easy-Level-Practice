def total_time(times: int, month: int):
    washing_time = 21
    months_to_day = month * 30
    time = times * months_to_day * washing_time
    time_min = time // 60
    time_sec = time % 60
    return f"{time_min} minutes and {time_sec} seconds"


print(total_time(8, 7))
print(total_time(8, 0))
print(total_time(7, 9))
