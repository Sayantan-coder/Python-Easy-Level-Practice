import math


def difference_area_square(radius: int) -> float:

    size_outer_square = 2 * radius
    size_inner_square = radius * math.sqrt(2)
    outer_square_area = size_outer_square**2
    inner_square_area = size_inner_square**2
    difference = outer_square_area - inner_square_area
    return round(difference, 0)


print(difference_area_square(7))
print(difference_area_square(6))
print(difference_area_square(5))
