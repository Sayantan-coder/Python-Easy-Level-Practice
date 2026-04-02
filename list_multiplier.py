def multiply(list_value: list) -> list:
    new_list = [[ch for ch in str(value) * len(list_value)] for value in list_value]
    return new_list


print(multiply([4, 5]))
print(multiply(["*", "%", "$"]))
print(multiply(["A", "B", "C", "D", "E"]))
