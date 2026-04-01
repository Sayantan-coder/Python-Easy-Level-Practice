def get_vertex_coordinates(coefficient_value: list) -> list:
    x_coordinate = round(-(coefficient_value[1] / (coefficient_value[0] * 2)), 2)
    y_coordinate = round(
        coefficient_value[2] - (coefficient_value[1] ** 2 / (coefficient_value[0] * 4)),
        2,
    )
    coordinate_list = [x_coordinate, y_coordinate]
    return coordinate_list


print(get_vertex_coordinates([1, 0, 25]))
print(get_vertex_coordinates([2, 7, 8]))
print(get_vertex_coordinates([1, 10, 4]))
