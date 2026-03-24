def flip_boolean(value: bool):
    if type(value) == bool:
        if value == True:
            value = False
            return value
        else:
            value = True
            return value
    else:
        return ValueError("boolean expected")


result = flip_boolean(True)
print(result)
