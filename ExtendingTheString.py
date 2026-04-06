def count_consonent(text: str) -> int:
    word = text.lower()
    count = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for char in word:
        if char not in vowels_list:
            if char.isalpha():
                count += 1
    return count


def count_vowel(text: str) -> int:
    word = text.lower()
    count = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for char in word:
        if char.isalpha():
            if char in vowels_list:
                count += 1
    return count


print(count_consonent("'Jameel SAEB'"))
print(count_vowel("He|\o mY Fr*end"))
print(count_consonent("Banerj ee"))
print(count_vowel("Sayantan"))
