def calculator(num1: int, opr: str, num2: int) -> float:
    if opr not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid operator! operator must be in between *,/,+,-")
    if opr == "/" and num2 == 0:
        raise ValueError("Can't divide by 0!")
    if opr == "+":
        return num1 + num2
    elif opr == "-":
        return num1 - num2
    elif opr == "*":
        return num1 * num2
    else:
        return num1 / num2


result_of_calculation = calculator(12, "*", 10)
print(result_of_calculation)
