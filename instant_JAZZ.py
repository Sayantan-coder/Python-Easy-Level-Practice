def create_newList(List: list) -> list:
    new_list = []
    for word in List:
        if str(7) in word:
            new_list.append(word)
        else:
            word1 = word + str(7)
            new_list.append(word1)
    return new_list


New_List = create_newList(["Sayantan", "g7", "h", "f7"])
print(New_List)
