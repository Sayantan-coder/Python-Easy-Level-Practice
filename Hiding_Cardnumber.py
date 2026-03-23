def card_hide(card: str):
    card_num = card[-4:]
    modified_card = ""
    length = len(card)
    for i in range(0, length - 4):
        modified_card = modified_card + "*"
    result = modified_card + card_num
    return result


print(card_hide("123498765"))
