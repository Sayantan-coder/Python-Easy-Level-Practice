def normalize_sentence(sentence: str) -> str:
    new_sentence = ""
    if sentence.isupper():
        for word in sentence:
            new_sentence += word.lower()
        return new_sentence + "!"
    else:
        for word in sentence:
            new_sentence += word
        return new_sentence


print(normalize_sentence("CAPS LOCK DAY IS OVER"))
print(normalize_sentence("Today is not caps lock day."))
print(normalize_sentence("Let us stay calm, no need to panic."))
