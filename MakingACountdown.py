def countdown(num: int, text: str) -> str:
    new_text = ""
    for number in range(num, 0, -1):
        new_text += str(number) + "."
    new_text = new_text + text.upper() + "!"
    return new_text


print(countdown(10, "Blast Off"))
print(countdown(3, "go"))
print(countdown(5, "FIRE"))
