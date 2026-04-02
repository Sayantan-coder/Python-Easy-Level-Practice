def sum_of_vowels(sentence: str):
    vowels_list = ["a", "e", "i", "o", "u"]
    vowels_dictionary = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 0}
    sum = 0
    for word in sentence:
        for char in word.lower():
            if char in vowels_list:
                sum += vowels_dictionary[char]
    return sum


print(sum_of_vowels("Let's test this function."))
print(sum_of_vowels("Do I get the correct output?"))
print(sum_of_vowels("I love edabit!"))
