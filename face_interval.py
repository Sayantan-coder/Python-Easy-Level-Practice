def face_interval(num_list: list) -> str:
    if type(num_list) != list:
        return ":/"
    else:

        def get_max_num(num_list):
            if len(num_list) == 1:
                return num_list[0]
            else:
                max = num_list[0]
                rest_max = get_max_num(num_list[1:])
                if max < rest_max:
                    return rest_max
                else:
                    return max

        def get_min_num(num_list):
            if len(num_list) == 1:
                return num_list[0]
            else:
                min = num_list[0]
                rest_min = get_min_num(num_list[1:])
                if rest_min < min:
                    return rest_min
                else:
                    return min

        difference = get_max_num(num_list) - get_min_num(num_list)
        if difference in num_list:
            return ":)"
        else:
            return ":("


print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval("bruh"))
