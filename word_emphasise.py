def emphasise(text: str) -> str:
    text_split = text.split(" ")
    new_text = " ".join([word[0].upper() + word[1:].lower() for word in text_split])
    return new_text


print(emphasise("hello world"))
print(emphasise("GOOD MORNING"))
print(emphasise("99 red balloons!"))
