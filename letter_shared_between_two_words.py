def shared_letter(word1: str, word2: str) -> int:
    count = 0
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                count += 1
    return f"shared lateer between {word1} and {word2} is {count}"


print(shared_letter("apple", "meaty"))
print(shared_letter("fan", "forsook"))
print(shared_letter("spout", "shout"))
