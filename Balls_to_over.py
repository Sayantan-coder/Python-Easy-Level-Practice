def balls_to_over(balls: int) -> float:
    overs = balls // 6
    ball = balls % 6
    return f"{overs}.{ball}"


print(balls_to_over(2400))
print(balls_to_over(164))
print(balls_to_over(945))
