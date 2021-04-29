def solution(A, x):
    result = -1
    missingPositions = x
    positions = {}
    i = 1
    while i<=x:
        positions[i] = 0
        i += 1
    
    for index, position in enumerate(A):
        print(index)
        if position in positions:
            del positions[position]
        if len(positions) < 1:
            result = index
            break

    return result

#print( solution([1,1,2], 2)) #2
print( solution([1,3,1,4,2,3,5,4],5)) #6