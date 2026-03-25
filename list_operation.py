def list_operation(num: int, num1: int, num2: int):
    List = []
    for i in range(num, num1 + 1):
        if i % num2 == 0:
            List.append(i)
    return List


print(list_operation(3, 15, 4))
