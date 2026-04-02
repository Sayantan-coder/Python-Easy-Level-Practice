def greeting(name: str) -> str:
    Guest_list = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina",
    }
    for key in Guest_list.keys():
        if key == name:
            country = Guest_list[key]
            break
        else:
            country = "guest"
    if country != "guest":
        return f"Hi! I'm {name}, and I'm from {country}."
    else:
        return f"Hi! I'm a {country}"


print(greeting("Randy"))
print(greeting("Sam"))
print(greeting("Monty"))
print(greeting("Wendy"))
