def get_thickness(layer: int) -> float:
    initial_thickness = 0.5

    thickness = initial_thickness
    for i in range(layer):
        thickness = thickness * 2
    result = thickness / 1000
    return result


thickness_of_paper = get_thickness(4)
print(thickness_of_paper)
