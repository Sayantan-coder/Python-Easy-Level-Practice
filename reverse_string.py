def ReverseString(word: str) -> str:
    temp1 = word
    temp = ""
    for index in range(len(temp1) - 1, -1, -1):
        temp += temp1[index]
        new_word = temp

    return new_word


reverse_word = ReverseString("Sayantan")
print(reverse_word)

