def age_difference(f_age: int, s_age: int) -> int:
    twice_age_year = 0
    difference = f_age - s_age
    if difference == s_age:
        return twice_age_year
    else:
        if difference < s_age:
            twice_age_year = s_age - difference
            return twice_age_year
        else:
            twice_age_year = difference - s_age
            return twice_age_year


print(age_difference(36, 7))
print(age_difference(50, 20))
print(age_difference(48, 22))
print(age_difference(42, 21))
