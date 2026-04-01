def stalactites_or_stalagmities(list2D: list) -> str:
    for i in range(len(list2D[0])):
        for j in range(len(list2D[len(list2D) - 1])):
            if list2D[0][i] == 1 and list2D[len(list2D) - 1][j] == 1:
                return "both"
            if list2D[0][i] == 1:
                return "Stalactites"
            if list2D[len(list2D) - 1][j] == 1:
                return "Stalagmites"


print(
    stalactites_or_stalagmities(
        [[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    )
)
print(
    stalactites_or_stalagmities(
        [[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
    )
)
print(
    stalactites_or_stalagmities(
        [[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
    )
)
