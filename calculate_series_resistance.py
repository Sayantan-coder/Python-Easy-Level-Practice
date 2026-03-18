def series_resistance(resist_list):
    Total_resistance = 0
    for resistance in resist_list:
        Total_resistance += resistance

    return Total_resistance


total_resistance = series_resistance([5, 7, 8, 9])
print(f"Total resistance in series circuit:{total_resistance}")
