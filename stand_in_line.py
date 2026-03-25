def update_list(List: list, num: int) -> list:
    new_list = []

    if len(List) == 0:
        return ValueError("No List has been selected")
    else:
        new_list = [List[i] for i in range(1, len(List))]
        new_list.append(num)
        return new_list


print(update_list([-1, 45, 5, 7, 8, 34, 0], 9))
