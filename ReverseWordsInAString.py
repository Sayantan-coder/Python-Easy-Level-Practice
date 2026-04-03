def reverse_words(text: str) -> str:
    text_list = text.split(" ")
    new_text = []
    for ind in range(len(text_list) - 1, -1, -1):
        new_text.append(text_list[ind])
    return " ".join(new_text).strip()


print(reverse_words("the sky is blue"))
print(reverse_words("  hello world!  "))
print(reverse_words("a good   example"))
