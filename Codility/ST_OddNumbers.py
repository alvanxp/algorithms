def contains_even_digits(number):
    even_numbers = {'2','4','6','8'}
    count = 0
    numberString = str(number)
    for c in numberString:
        if c in even_numbers:
            count += 1
    return count >= 2

print(contains_even_digits(24))
print(contains_even_digits(21))
print(contains_even_digits(1))
print(contains_even_digits(-21))
print(contains_even_digits(-24))

