def showdown(word1: str, word2: str) -> str:
    count = 0
    count1 = 0
    for i in range(0, len(word1)):
        if word1[i] == " ":
            count += 1
        else:
            break
    for j in range(0, len(word2)):
        if word2[j] == " ":
            count1 += 1
        else:
            break
    if count < count1:
        return "word1"
    elif count == count1:
        return "tie"
    else:
        return "word2"


winner = showdown("  s  a yantan", "   s  ayan tan")
print(winner)
