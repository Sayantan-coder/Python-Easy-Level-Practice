def is_PinValid(value=None) -> bool:
    if value == None:
        return False
    elif len(value) == 4 or len(value) == 6:
        return True
    else:
        return False


print(is_PinValid("2345@"))
