def largest_number(f, g):
    value_f = f()
    value_g = g()
    if value_f > value_g:
        return "f"
    elif value_f == value_g:
        return "neither"
    else:
        return "g"


print(largest_number(lambda: 5, lambda: 10))
print(largest_number(lambda: 25, lambda: 25))
print(largest_number(lambda: 505050, lambda: 5050))
