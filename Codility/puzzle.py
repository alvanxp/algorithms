import math
def solution(A):
    # write your code in Python 3.6
    sum = 0
    min_rest = 100000
    left = A[0]
    for a in A:
        sum += a

    for i in range(1, len(A)):        
        rigth = sum - left        
        min_rest = min(abs(left - rigth), min_rest)
        left += A[i]
    return min_rest

print(solution([-1000, 1000]))
