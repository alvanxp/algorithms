def solution(A):
    max_sum = 0
    starting_here = [0] * len(A)
    starting_here[len(A)-1] = A[len(A)-1]
    for idx in reversed(range(len(A)-1)):
        starting_here[idx] = max(starting_here[idx+1], A[idx])

    for idx in range(len(A)-2):
        max_sum = max(starting_here[idx+2] + A[idx], max_sum)

    return max_sum
    
print(solution([1,8,2,4,1]))#12
print(solution([1,0,-2,1,1]))#2
print(solution([10,8,6,4,2]))#16
print(solution([1,2,3,4,5]))#8
print(solution([1,-1,1,-1,1]))#2
