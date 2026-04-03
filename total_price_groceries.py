def calculate_total_price(grocery_list: list) -> float:
    total_price = 0
    for groceries in grocery_list:
        total_price = total_price + (groceries["quantity"] * groceries["price"])
    return round(total_price, 1)


print(
    calculate_total_price(
        [
            {"product": "Milk", "quantity": 1, "price": 1.50},
            {"product": "Cereals", "quantity": 1, "price": 2.50},
        ]
    )
)
print(calculate_total_price([{"product": "Milk", "quantity": 3, "price": 1.50}]))
print(
    calculate_total_price(
        [
            {"product": "Milk", "quantity": 1, "price": 1.50},
            {"product": "Eggs", "quantity": 12, "price": 0.10},
            {"product": "Bread", "quantity": 2, "price": 1.60},
            {"product": "Cheese", "quantity": 1, "price": 4.50},
        ]
    )
)
print(
    calculate_total_price(
        [
            {"product": "Chocolate", "quantity": 1, "price": 0.10},
            {"product": "Lollipop", "quantity": 1, "price": 0.20},
        ]
    )
)
