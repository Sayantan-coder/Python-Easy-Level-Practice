import math


def solution_of_quadratic_equation(a, b, c):
    discriminent = (b**2) - (4 * a * c)
    neumarator = -(b) + math.sqrt(discriminent)
    root_value = neumarator / 2 * a
    return round(root_value, 0)


print(solution_of_quadratic_equation(1, 2, -3))
print(solution_of_quadratic_equation(2, -7, 3))
print(solution_of_quadratic_equation(1, -12, -28))
