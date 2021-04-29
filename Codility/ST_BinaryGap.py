def get_max_binarygap(number):
    number_as_binary = "{0:b}".format(number)
    result = 0

    isZero = False
    count = 0
    for digit in number_as_binary:
        if digit == '0':
            isZero = True
            count += 1
        else:
            result = max(result, count)
            count = 0
            isZero = False
    return result

print(get_max_binarygap(9)) #2
print(get_max_binarygap(1041)) #5
print(get_max_binarygap(32)) #0

         


