def split_number(num: int):
    left = num // 2
    right = num - left
    split_list = [left, right]
    return split_list


splited_number = split_number(46)
print(splited_number)
