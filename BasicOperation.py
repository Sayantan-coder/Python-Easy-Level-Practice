def operation(op1: str, op2: str, operator: str) -> str:
    operators_list = ["add", "subtract", "mul", "divide"]
    if operator not in operators_list:
        return ValueError("Operatoes must be in between add, subtract, mul and divide")
    else:
        if int(op2) == 0 and operator == "divide":
            return "undefined"
        if operator == "add":
            return str(int(op1) + int(op2))
        elif operator == "subtract":
            return str(int(op1) - int(op2))
        elif operator == "mul":
            return str(int(op1) * int(op2))
        else:
            return str(int(op1) // int(op2))


print(operation("20", "5", "mul"))
print(operation("1", "2", "add"))
print(operation("4", "5", "subtract"))
print(operation("6", "3", "divide"))
