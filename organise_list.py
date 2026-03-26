def organise_list(num_list: list) -> list:
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)
    sorted_list = sorted(unique_list)
    return sorted_list


print(organise_list([34, 56, 56, 43, 12, 12, 90]))
