def percentage_to_decimal(value: list) -> list:
    number = [float(i.replace("%", "")) for i in value]
    new_list = [val / 100 for val in number]
    return new_list


print(percentage_to_decimal(["33%", "98.1%", "56.44%", "100%"]))
