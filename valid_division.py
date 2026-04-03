def is_valid_division(division_equation) -> bool:
    equation = division_equation.split("/")
    if int(equation[1]) == 0:
        return ValueError("Invalid")
    else:
        if int(equation[0]) % int(equation[1]) == 0:
            return True
        else:
            return False


print(is_valid_division("6/2"))
print(is_valid_division("11/5"))
print(is_valid_division("0/3"))
print(is_valid_division("3/0"))
