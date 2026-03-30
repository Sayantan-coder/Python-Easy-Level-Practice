def calculate_profit(inventory: dict) -> int:
    total_profit = (inventory["sell_price"] * inventory["items"]) - (
        inventory["cost_price"] * inventory["items"]
    )
    return f"{total_profit:.0f}"


print(calculate_profit({"cost_price": 32.67, "sell_price": 45.00, "items": 1200}))
print(calculate_profit({"cost_price": 225.89, "sell_price": 550.00, "items": 100}))
print(calculate_profit({"cost_price": 2.77, "sell_price": 7.95, "items": 8500}))
