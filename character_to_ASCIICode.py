def char_to_ASCIICode(char_list: list) -> list:
    ASCIICode_list = []
    for char in char_list:
        ASCIICode_list.append({char: ord(char)})
    return ASCIICode_list


print(char_to_ASCIICode(["s", "a", "y", "a", "n", "t", "a", "n"]))
print(char_to_ASCIICode(["b", "a", "n", "e", "r", "j", "e", "e"]))
print(char_to_ASCIICode(["!", "@", "#", "$", "%"]))
print(char_to_ASCIICode([]))
