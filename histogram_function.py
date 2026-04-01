def histogram_function(value_list: list, char: str):
    pattern = ""

    for value in value_list:
        element = char * value
        pattern = pattern + element + "\n"

    return pattern.strip()


# value_list = [1, 5, 3]

print(histogram_function([1, 3, 4], "#"))
print(histogram_function([6, 2, 15, 3], "="))
print(histogram_function([1, 10], "+"))
