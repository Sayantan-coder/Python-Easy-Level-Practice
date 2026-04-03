def get_missing_letters(word: str) -> str:
    letters_list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "i",
        "o",
        "u",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    missing_letters = ""
    word_list = list(word)

    for char in letters_list:
        if char not in word_list:
            missing_letters += char
    return "".join(sorted(missing_letters))


print(get_missing_letters("abcdefgpqrstuvwxyz"))
print(get_missing_letters("zyxwvutsrq"))
print(get_missing_letters("abc"))
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz"))
