class OnesThreesNines:
    def __init__(self, num: int):
        self.ones = num // 1
        self.threes = num // 3
        self.nines = num // 9


n1 = OnesThreesNines(25)
print(n1.ones)
print(n1.threes)
print(n1.nines)
