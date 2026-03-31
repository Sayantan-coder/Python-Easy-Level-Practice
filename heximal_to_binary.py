def hex_to_binary(num_str: str) -> str:
    def hex_to_decimal(num_str: str) -> int:
        hex_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
        }
        decimal = 0
        power = 0

        for num in reversed(num_str.upper()):
            value = hex_map[num]
            mul = 1

            for _ in range(power):
                mul *= 16

            decimal += value * mul
            power += 1

        return decimal

    def decimal_to_binary(decimal: int) -> str:
        if decimal == 0:
            return "0"

        bit_list = []
        while decimal:
            bit_list.append(str(decimal % 2))
            decimal //= 2

        return "".join(reversed(bit_list))

    return decimal_to_binary(hex_to_decimal(num_str))


print(hex_to_binary("43FF"))
print(hex_to_binary("AF64"))
print(hex_to_binary("5FA"))
