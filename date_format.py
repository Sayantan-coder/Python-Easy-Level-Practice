def format_date(date: str) -> str:
    date_list = date.split("/")
    format_date = "".join(date_list[i] for i in range(2, -1, -1))
    return f"{format_date}"


print(format_date("30/03/2026"))
print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))
