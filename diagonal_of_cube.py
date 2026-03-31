import math


def get_diagonal(value: float) -> float:
    side = value ** (1 / 3)
    diagonal_cube = side * math.sqrt(3)
    return round(diagonal_cube, 2)


print(get_diagonal(8))
print(get_diagonal(343))
print(get_diagonal(1157.625))
