def color_invert(rgb):
    rgb_list = list(rgb)
    print(rgb_list)
    newvalue = tuple([255 - i for i in rgb_list]) # list comprehension
    return newvalue


result = color_invert((165, 170, 221))
print(result)
