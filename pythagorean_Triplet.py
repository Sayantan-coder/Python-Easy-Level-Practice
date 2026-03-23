def is_triplet(num1: float, num2: float, num3: float) -> bool:
    list = [num1, num2, num3]
    sorted_list = sorted(list)
    exp1 = (sorted_list[0] * sorted_list[0]) + (sorted_list[1] * sorted_list[1])
    exp2 = sorted_list[2] * sorted_list[2]
    if exp1 == exp2:
        return True
    return False


print(is_triplet(3, 5, 4))
