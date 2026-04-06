def count_uppercase(words_list: list) -> int:
    count = 0
    for word in words_list:

        for char in word:
            if char.isupper():
                count += 1
    return count


print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))
print(count_uppercase(["little", "lower", "down"]))
print(count_uppercase(["EDAbit", "Educate", "Coding"]))
