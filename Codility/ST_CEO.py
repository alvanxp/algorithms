def ceo_visit(A, X):
    seen = [False] * X
    uncovered = X
 
    for idx in range(len(A)):
        if seen[A[idx]-1] == False:
            seen[A[idx]-1] = True
            uncovered -= 1
            if uncovered == 0:
                return idx + 1
 
    return -1

print(ceo_visit([1,3,1,4,2,3,5,4], 5))