import math


def get_length(point1: list, point2: list) -> float:
    value = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
    result = math.sqrt(value)
    return round(result, 2)


print(get_length([15, 7], [22, 11]))
print(get_length([0, 0], [0, 0]))
print(get_length([0, 0], [1, 1]))
