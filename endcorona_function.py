import math


def end_corona(recover_cases, new_cases, active_cases):
    net_decrease = recover_cases - new_cases
    time = math.ceil(active_cases / net_decrease)
    return time


end_corona_time = end_corona(3200, 2000, 6000)
print(end_corona_time)
# Using While loop:-


def end_corona(recover_cases, new_cases, active_cases):
    net_decrease_perday = recover_cases - new_cases
    day_count = 0
    while active_cases > 0:
        active_cases -= net_decrease_perday
        day_count += 1
    return day_count


end_corona_time = end_corona(4000, 2000, 77000)
print(end_corona_time)
