def parallel_resistance(resist_list):
    result = 0
    for resistance in resist_list:
        result += 1 / resistance
    Result = 1 / result
    return Result


total_resistance_parallel = parallel_resistance([2, 4, 6, 8])
print(f"Total resistance in parallel:{total_resistance_parallel}")
