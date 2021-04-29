def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    count = 0
    result = 0
    for k in range(n):
        if (A[k] == candidate):            
            count += 1
    left = 0
    right = 0
    for k in range(n):
        if (A[k] == candidate):                    
            left += 1
        right = count - left
        l = left > (k+1) // 2
        r = right > (n - (k+1))//2
        if l and r :
            result +=1            
            
    return result
#print(goldenLeader([4, 4, 2, 5, 3, 4, 4, 4]))
print(goldenLeader([4,3,4,4,4,2]))
#print(goldenLeader([3,1,1,2,1,1,3,1]))