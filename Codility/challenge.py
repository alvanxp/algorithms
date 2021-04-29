import sys
def solution(A):
    n = len(A)
    min_distance = sys.maxsize 
    current = A[0]
    start = 0
    for i in range(start+1,n):
        if A[i] - current > 1:
            min_distance = min(min_distance,A[i] - current )


    return min_distance

print(solution([0,3,3,7,5,3,11,1]))

