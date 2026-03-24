def get_hamming_distance(word1: str, word2: str) -> int:
    distance = 0
    for i, (char1, char2) in enumerate(zip(word1, word2)):
        if char1 != char2:
            distance += 1
    return distance


hamming_distance = get_hamming_distance("mango", "mouse")
print(hamming_distance)
