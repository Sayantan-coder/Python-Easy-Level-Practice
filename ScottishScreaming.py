def to_scottish_screaming(text: str) -> str:
    cap_text = text.upper()
    vowel_list = ["A", "E", "I", "O", "U"]
    new_text = ""
    for ind in range(len(cap_text)):
        if cap_text[ind] in vowel_list:
            # cap_text[ind] = "E"
            replace_vowel = cap_text[ind].replace(cap_text[ind], "E")
            new_text += replace_vowel
        else:
            new_text += cap_text[ind]
    return new_text


print(to_scottish_screaming("hello world"))
print(to_scottish_screaming("Mr. Fox was very naughty"))
print(to_scottish_screaming("Butterflies are beautiful!"))
