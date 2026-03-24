def count_character(List: list):
    count = 0
    for element in List:
        for char in element:
            count += 1

    return count


number_of_characters = count_character(["sayantan", "suman"])
print(number_of_characters)
