def pattern_design(m: int, n: int, s: str = "#") -> list:
    pattern_list = []
    for i in range(m):
        element = ""
        for j in range(1, n + 1):
            element += s
        pattern_list.append(element)
    return pattern_list


print(pattern_design(5, 3, "@"))
