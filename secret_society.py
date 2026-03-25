def society_name(List: list) -> str:
    name_list = sorted(List)
    Name = ""
    for name in name_list:
        Name += name[0]
    society_name = Name.upper()
    return society_name


print(society_name(["Sayantan", "Suman", "Debasish", "Souvik", "Proloy"]))
