def neutralise(str1: str, str2: str):
    new_string = ""
    for char1, char2 in zip(str1, str2):
        if char1 == char2 == "+":
            new_string += char1
        elif char1 == char2 == "-":
            new_string += char1
        else:
            new_string += "0"
    return new_string


print(neutralise("--++--", "++--++"))
print(neutralise("-+-+-+", "-+-+-+"))
print(neutralise("-++-", "-+-+"))
