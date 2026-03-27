def is_adjacent(matrix, node1, node2) -> bool:
    if (node1 and node2) in range(len(matrix) - 1):
        if matrix[node1][node2] == 1:
            return True
        else:
            return False


result = is_adjacent([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 0, 1)
print(result)
