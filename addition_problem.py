def get_addition(value1, value2):
    if type(value1) != type(value2):
        return None
    else:
        if type(value1) == int and type(value2) == int:
            val1 = str(value1)
            val2 = str(value2)
            return val1 + val2
        else:
            num1 = int(value1)
            num2 = int(value2)
            return num1 + num2


print(get_addition(1, 2))
print(get_addition("1", "2"))
print(get_addition("1", 2))
