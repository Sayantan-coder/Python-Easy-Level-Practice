def longest_time(hour: int, min: int, sec: int):
    hour_time = hour * 3600
    min_time = min * 60
    sec_time = sec
    if hour_time > min_time:
        if hour_time > sec_time:
            return hour
        else:
            return sec
    else:
        if min_time > sec_time:
            return min
        else:
            return sec


print(longest_time(1, 59, 3598))
print(longest_time(2, 300, 15000))
print(longest_time(15, 955, 59400))
