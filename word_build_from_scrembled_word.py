def new_word(word_list: list, pos_list: list) -> str:
    new_word = ""
    for pos in pos_list:
        new_word = new_word + word_list[pos]
    return new_word


print(new_word(["g", "e", "o"], [1, 0, 2]))
print(new_word(["e", "t", "s", "t"], [3, 0, 2, 1]))
print(new_word(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]))
