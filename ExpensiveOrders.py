def get_expensive_orders(order_list: dict, cost: int) -> dict:
    expensive_orders = {}
    for order in order_list:
        if order_list[order] > cost:
            expensive_orders[order] = order_list[order]
    return expensive_orders


print(get_expensive_orders({"a": 3000, "b": 200, "c": 1050}, 1000))
print(
    get_expensive_orders(
        {
            "Gucci Fur": 24600,
            "Teak Dining Table": 3200,
            "Louis Vutton Bag": 5550,
            "Dolce Gabana Heels": 4000,
        },
        20000,
    )
)
print(get_expensive_orders({"Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5}, 40))
