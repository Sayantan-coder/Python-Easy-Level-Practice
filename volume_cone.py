import math


def get_volume(height: float, radius: float) -> float:
    Volume_of_cone = math.pi * radius * radius * (height / 3)
    result = round(Volume_of_cone, 2)
    return result


print(get_volume(15, 6))
