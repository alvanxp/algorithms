def find_alone_number(A):
    result = 0
    totalsForNumber = {}
    for number in A:
        if number not in totalsForNumber:
            totalsForNumber[number] = 0
        totalsForNumber[number] += 1
    print(totalsForNumber)
    
    for counterForNumber in totalsForNumber:
        if totalsForNumber[counterForNumber] % 2 == 1:
            result = counterForNumber
            break
    return result

print(find_alone_number([1,2,1])) #2
print(find_alone_number([9,3,9,3,9,9,7,7,7])) #7
print(find_alone_number([1])) #1