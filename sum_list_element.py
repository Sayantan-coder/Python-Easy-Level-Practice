def get_sum_listelement(num_list: list) -> list:
    new_list = []
    sum_list = []
    for ind in range(len(num_list)):
        New_list = num_list[:ind] + num_list[ind + 1 :]
        new_list.append(New_list)
    for value in new_list:
        sum = 0
        for num in value:
            sum += num
        sum_list.append(sum)
    return sum_list


print(get_sum_listelement([1, 2, 3, 2, 1]))
print(get_sum_listelement([1, 2]))
print(get_sum_listelement([1, 2, 3]))
print(get_sum_listelement([1, 2, 3, 4, 5]))
print(get_sum_listelement([10, 20, 30, 40, 50, 60]))
