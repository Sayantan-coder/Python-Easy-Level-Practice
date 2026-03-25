def is_order(text: str) -> bool:
    word = "".join(sorted(text.lower()))
    if word == text.lower():
        return True
    return False


print(is_order("Abcdef"))
