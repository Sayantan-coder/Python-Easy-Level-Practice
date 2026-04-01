def return_unique(num_list: list) -> list:
    unique_list = []
    for i in range(len(num_list)):
        count = 0
        for j in range(len(num_list)):
            if num_list[i] == num_list[j]:
                count += 1
        if count == 1:
            unique_list.append(num_list[i])
    return unique_list


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
