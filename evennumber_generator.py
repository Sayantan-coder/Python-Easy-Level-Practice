def get_evennumber(num: int) -> list:
    List = [i for i in range(1, num + 1) if i % 2 == 0]
    return List


even_numbers = get_evennumber(20)
print(even_numbers)
