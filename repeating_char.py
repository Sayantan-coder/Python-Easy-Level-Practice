def double_char(word: str) -> str:
    new_word = ""
    for char in word:
        new_word += 2 * char
    return new_word


print(double_char("Mango @4 fruit"))
