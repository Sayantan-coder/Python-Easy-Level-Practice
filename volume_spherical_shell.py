import math


def get_volume(inner_radius, outer_radius):
    if inner_radius > outer_radius:
        inn_radius = outer_radius
        out_radius = inner_radius
        radius_difference = (out_radius**3) - (inn_radius**3)
        volume = (4 * math.pi * radius_difference) / 3
        return round(volume, 3)
    else:
        radius_difference = (outer_radius**3) - (inner_radius**3)
        volume = (4 * math.pi * radius_difference) / 3
        return round(volume, 3)


print(get_volume(3, 3))
print(get_volume(7, 2))
print(get_volume(3, 800))
