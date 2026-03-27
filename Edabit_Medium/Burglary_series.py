def find(items: dict, name: str) -> str:
    key_list = []
    for key in items.keys():
        key_list.append(key)
    if name in key_list:
        return f"{name[0].upper()+name[1:]} is gone ..."
    else:
        return f"{name[0].upper()+name[1:]} is here!"


print(find({"tommy": 1, "tv": 9, "dog": 8, "box": 7}, "dog"))
