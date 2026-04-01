def box_sequence(steps: int = 0) -> int:
    box_sequence = 0
    for step in range(1, steps + 1):
        if step % 2 != 0:
            box_sequence += 3
        else:
            box_sequence -= 1
    return box_sequence


print(box_sequence(7))
print(box_sequence(6))
print(box_sequence(1))
print(box_sequence())
