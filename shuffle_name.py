def name_shuffle(name: str) -> str:
    split_value = name.split(" ")
    reverse_split = [split_value[i] for i in range(len(split_value) - 1, -1, -1)]
    reverse_name = " ".join(reverse_split)
    return reverse_name


shuffle_name = name_shuffle("sayantan banerjee")
print(shuffle_name)
