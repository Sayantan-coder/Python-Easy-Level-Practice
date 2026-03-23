import datetime


def datetime_function(date) -> bool:
    if date.month == 12 and date.day == 24:
        return True
    else:
        return False


print(datetime_function(datetime.date(2025, 10, 24)))
