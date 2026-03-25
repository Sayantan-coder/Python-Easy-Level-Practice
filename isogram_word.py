def is_isogram(word: str) -> bool:
    name = word.lower()
    word1 = ""
    for char in name:
        if char not in word1:
            word1 += char
        else:
            return False
    return True


result = is_isogram("Mango")
print(result)
