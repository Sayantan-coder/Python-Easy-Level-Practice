def replace_vowels(text: str, char: str) -> str:
    modified_text = ""
    vowels_list = ["a", "e", "i", "o", "u"]
    for word in text:
        if word in vowels_list:
            modified_text = modified_text + char
        else:
            modified_text = modified_text + word
    return modified_text


Replace_Vowels = replace_vowels("I am a boy", "@")
print(Replace_Vowels)
