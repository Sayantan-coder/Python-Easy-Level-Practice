def count_unique_char(word: str) -> int:
    temp = ""
    count = 0
    for i in word:
        if i in temp:
            pass
        else:
            temp = temp + i
            count = count + 1
            # print(temp)
    return count


Unique_char_word = count_unique_char("Debasish")
print(Unique_char_word)
