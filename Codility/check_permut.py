def solution(A):
    n = len(A)
    h = [False] * (n + 1)
    for i in range(n):
        if (A[i] > n):
            return 0
        h[A[i]] = True
    for i in range(1, len(h)):
        if (not h[i]):
            return 0
    return 1

print(solution([4, 1, 3, 2]))