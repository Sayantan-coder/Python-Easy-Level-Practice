def get_area_country(country: str, area: int) -> str:
    world_landmass = 148940000
    fraction_percentage = (area / world_landmass) * 100
    return f"{country} is {fraction_percentage:.2f}% of the total world's landmass"


print(get_area_country("India", 23567890))
print(get_area_country("Russia", 17098242))
print(get_area_country("USA", 9372610))


print(get_area_country("Iran", 1648195))
