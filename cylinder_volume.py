import math


def cylinder_volume(radius: float, height: float) -> float:
    volume = (math.pi * radius * radius * height) / 1000
    result = round(volume, 2)
    return result


mass_of_cylinder = cylinder_volume(30, 60)
print(mass_of_cylinder)
