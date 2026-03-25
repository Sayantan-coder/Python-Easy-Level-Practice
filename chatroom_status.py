def status(List: list) -> str:
    length = len(List)
    if length == 0:
        return "no one online"
    elif length == 1:
        return f"{List[0]} online"
    elif length == 2:
        return f"{List[0]} and {List[1]} online"
    else:
        return f"{List[0]}, {List[1]} and {length - 2} more online"


print(status(["Sayantan", "Sourish", "deep", "puja", "sayan"]))
