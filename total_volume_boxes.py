def total_volume(*boxes: tuple) -> float:
    total_volume = 0
    for box in boxes:
        for value in box:
            volume = value * value * value
        total_volume += volume
    return total_volume


print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
print(total_volume([2, 2, 2], [2, 1, 1]))
print(total_volume([1, 1, 1]))
