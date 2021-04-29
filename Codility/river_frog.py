def solution(X, A):
    n = len(A)
    h = [False] * X
    for i in range(0, n):
        if ( A[i] < h[A[i]] or A[i] > -1 ):
            h[A[i]] = i
    
    return h[X] 

#print(solution(2, [2,2,2,2,2,2,]))
#print(solution(2, [2]))
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

