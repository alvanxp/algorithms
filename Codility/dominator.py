def goldenLeader(A):
    n = len(A)
    size = 0
    idx = -1
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
    for k in range(n):
        if (A[k] == candidate):
            count += 1
            idx = k
    if (count > n // 2):
        return idx
    return -1
# print(goldenLeader([4,6,6,6,6,8]))
print(goldenLeader([3,1,1,2,1,1,3,1]))