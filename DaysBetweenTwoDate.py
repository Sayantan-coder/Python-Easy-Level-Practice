import datetime


def get_days(date1: str, date2: str) -> int:
    year_difference = date2.year - date1.year
    month_difference = date2.month - date1.month
    day_difference = date2.day - date1.day
    total_days_difference = (
        (year_difference * 365) + (month_difference * 30) + day_difference
    )
    return total_days_difference


print(get_days(datetime.date(2019, 6, 14), datetime.date(2019, 6, 20)))
print(get_days(datetime.date(2018, 12, 29), datetime.date(2019, 1, 1)))
print(get_days(datetime.date(2020, 5, 24), datetime.date(2019, 5, 24)))
