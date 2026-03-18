def discount_price(price: int, discount: int) -> int:
    result = price - (price * discount / 100)
    return result


price_after_discount = discount_price(1500, 70)
print(f"price after discount: {price_after_discount}")
