def filter_list(value: list) -> list:
    new_list = []
    for i in value:
        if type(i) == int:
            new_list.append(i)
    return new_list


FilterList = filter_list([12, 32, 43, "abc", "cds", 87, "45", "man"])
print(FilterList)
