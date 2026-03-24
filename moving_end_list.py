def move_to_end(List, j):
    new_list = [item for item in List if item != j] + [num for num in List if num == j]
    return new_list


modified_list = move_to_end([12, 45, 0, 1, 34, 2, "j", 2, "f"], 2)
print(modified_list)
