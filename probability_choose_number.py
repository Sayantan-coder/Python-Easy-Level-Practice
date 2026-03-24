def prob_choose_number(List: list, value: int) -> float:
    length_List = len(List)
    count_num = 0
    for num in List:
        if num >= value:
            count_num += 1
    probability = (count_num / length_List) * 100
    result = f"probability of choose a number:{probability:.1f} "
    return result


print(prob_choose_number([2, 3, 6, 7, 9], 4))
