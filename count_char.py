def count_char(word: str) -> bool:
    count1 = 0
    count2 = 0

    for char in word:
        if char == "x":
            count1 = count1 + 1
        elif char == "o":
            count2 = count2 + 1
    if count1 == count2:
        return True
    else:
        return False


print(count_char("pzzpoorxxea"))
