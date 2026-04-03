def next_letter(text: str) -> str:
    word_dictionary = {
        "a": "b",
        "b": "c",
        "c": "d",
        "d": "e",
        "e": "f",
        "f": "g",
        "g": "h",
        "h": "i",
        "i": "j",
        "j": "k",
        "k": "l",
        "l": "m",
        "m": "n",
        "n": "o",
        "o": "p",
        "p": "q",
        "q": "r",
        "r": "s",
        "s": "t",
        "t": "u",
        "u": "v",
        "v": "w",
        "w": "x",
        "x": "y",
        "y": "z",
    }
    new_text = ""
    for char in text:
        if char in word_dictionary.keys():
            next_char = word_dictionary[char]
            new_text += next_char
    return new_text


print(next_letter("bye"))
print(next_letter("sayantan"))
print(next_letter("welcome"))
