def get_index_caps(word: str) -> list:
    index_list = []
    for index in range(0, len(word)):
        if word[index].isupper() == True:
            index_list.append(index)
    return index_list


CapitalLetter_Index_List = get_index_caps("SaYAntaN")
print(CapitalLetter_Index_List)
