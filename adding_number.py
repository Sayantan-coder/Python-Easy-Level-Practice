def adding_number(str1: str, str2: str) -> str:
    if str1 == "" or str2 == "":
        return ValueError("Invalid Operation")
    else:
        num1 = int(str1)
        num2 = int(str2)
        result = num1 + num2
        return str(result)


print(adding_number("450", "250"))
print(adding_number("111", "111"))
print(adding_number("10", "80"))
print(adding_number("", "20"))
