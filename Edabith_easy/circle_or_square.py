import math


def Circle_or_Square(radius: int, area: int) -> bool:
    circumference = 2 * math.pi * radius
    perimeter = 4 * math.sqrt(area)
    if circumference > perimeter:
        return True
    return False


result = Circle_or_Square(5, 64)
print(result)
