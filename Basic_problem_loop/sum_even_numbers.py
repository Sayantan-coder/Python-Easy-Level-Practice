def SumEvenNumber():
    sum = 0
    for num in range(1, 101):
        if num % 2 == 0:
            sum = sum + num
    return sum


sum_of_even_numbers = SumEvenNumber()
print(sum_of_even_numbers)


# Sum of odd numbers :-
def SumOddNumber():
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            continue
        else:
            sum = sum + i
    return sum


sum_of_odd_numbers = SumOddNumber()

print(sum_of_odd_numbers)
