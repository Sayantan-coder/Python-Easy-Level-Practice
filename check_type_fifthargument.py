def type_of_fifthArgument(*values):
    if len(values) < 5:
        return ValueError("Not enough arguments")
    else:
        data_type = type(values[4])
        return data_type


print(type_of_fifthArgument(1, 2, 3, 4, 5))
print(type_of_fifthArgument("a", 2, 3, [1, 2, 3], "five"))
print(type_of_fifthArgument())
