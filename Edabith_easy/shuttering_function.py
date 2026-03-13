def shutter(word):
    first_two_char = word[:2] + "... "
    x = first_two_char + first_two_char
    result = x + word + "?"
    return result


y = shutter("Sayantan")
print(y)
