def get_ASCIICode(char: str) -> int:
    Value = char.swapcase()
    return ord(Value)


print(get_ASCIICode("a"))
