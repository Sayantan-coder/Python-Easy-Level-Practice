def correct_sign(exp):
    result = eval(exp)
    if result == True:
        return True
    else:
        return False


print(correct_sign("45>7<67"))
