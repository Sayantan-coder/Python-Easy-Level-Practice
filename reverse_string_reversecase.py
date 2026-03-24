def reverse(word: str) -> str:
    word1 = word.swapcase()
    new_word = list(reversed((word1)))
    reverse_string = "".join(new_word)
    return reverse_string


print(reverse("sayantAN baNerjee"))
