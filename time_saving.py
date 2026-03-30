def save_time(speed_limit, avg_speed, distance):
    time_actual = distance / avg_speed
    time_limit = distance / speed_limit
    save_time = (time_limit - time_actual) * 60
    return f"{save_time:.1f}"


print(save_time(80, 90, 40))
print(save_time(80, 90, 4000))
print(save_time(80, 100, 40))
print(save_time(80, 100, 10))
