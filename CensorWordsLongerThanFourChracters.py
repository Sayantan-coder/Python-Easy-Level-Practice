def censor(text: str) -> str:
    words_list = text.split(" ")
    new_text = []
    for word in words_list:
        if len(word) > 4:
            new_text.append(word.replace(word, "*" * len(word)))
        else:
            new_text.append(word)
    return " ".join(new_text)


print(censor("The code is fourty"))
print(censor("Two plus three is five"))
print(censor("aaaa aaaaa 1234 12345"))
