import math


def Radian(degree):
    radian = (degree * math.pi) / 180
    return radian


Result = Radian(30)
print(f"{Result:.1f}")
