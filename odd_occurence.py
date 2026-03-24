def getOddOccurence(value: list):
    for i in range(0, len(value)):
        count = 0
        for j in range(0, len(value)):
            if value[i] == value[j]:
                count += 1
        if count % 2 != 0:
            return value[i]
    return -1


Odd_Occurence_Number = getOddOccurence([23, 23, 43, 56, 56, 7, 8, 8, 7])
print(Odd_Occurence_Number)
