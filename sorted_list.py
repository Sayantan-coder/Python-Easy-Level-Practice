def sorted_list(list, word):
    if word not in ["Asec", "Desc", "None"]:
        raise ValueError("Invalid Word!,Word must be in Asec, Desc,None")
    else:
        if word == "Asec":
            return sorted(list)
        elif word == "Desc":
            return sorted(list, reverse=True)
        else:
            return list


Sorted_List = sorted_list([45, 78, 34, 23], "Desc")
print(Sorted_List)
