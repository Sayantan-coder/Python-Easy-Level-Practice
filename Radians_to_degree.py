import math


def Radians_to_degree(x):
    result = (x * 180) / math.pi
    return result


y = Radians_to_degree(50)
print(f"{y:.2f}")


# Second Method:-
def degree(rad):
    result = math.degrees(rad)
    return result


Radians_to_degree = degree(50)
print(f"{Radians_to_degree:.2f}")
