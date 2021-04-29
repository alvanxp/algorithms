def max_sum(A):
    n = len(A)
    inc = A[0]
    exc = 0    
    for a in A[1:]:
        exc_new = max(inc, exc)
        inc = exc + a
        exc = exc_new
    return max(inc, exc)

print(max_sum([5,4,3,2,0,3]))