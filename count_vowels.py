def count_vowels(word: str) -> int:
    count = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for char in word:
        if char in vowels_list:
            count = count + 1

    return count


number_of_vowels = count_vowels("ashim")
print(number_of_vowels)
