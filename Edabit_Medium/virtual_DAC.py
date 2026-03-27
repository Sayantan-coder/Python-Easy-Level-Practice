def get_DAC(value: int) -> float:
    fraction_value = value / 1023
    voltage = fraction_value * 5
    return f"voltage is {voltage:.2f}"


print(get_DAC(0))
print(get_DAC(1023))
print(get_DAC(400))
