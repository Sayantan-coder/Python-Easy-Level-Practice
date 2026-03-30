def length_of_string(word: str) -> int:
    count = 0
    while word:
        count += 1
        word = word[1:]
    return count


print(length_of_string("sayantan"))
print(length_of_string(""))
print(length_of_string("mango"))
