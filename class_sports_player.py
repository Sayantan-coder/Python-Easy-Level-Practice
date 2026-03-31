class PlayerInformation:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is {self.age} age."

    def get_weight(self):
        return f"{self.name} is {self.weight} kg."

    def get_height(self):
        return f"{self.name} is {self.height} cm."


P1 = PlayerInformation("Sayantan", 23, 178, 70)
print(P1.get_age())
print(P1.get_weight())
print(P1.get_height())
