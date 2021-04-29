def solution(U, L, C):
    n = len(C)
    r = [[0] * n for i in range(2)]
    for i in range((n // 2)+1):
        left= C[i]
        right = C[n-1-i]
        if U > 0 and left > 0:
            r[0][i] = 1
            U -= 1
            left -= 1
        if U > 0 and right > 0:
            r[0][n-1-i] = 1
            U -= 1
            right -= 1     
        if L > 0 and left > 0:
            r[1][i] = 1
            L -= 1
            left -= 1
        if L > 0 and right > 0:
            r[1][n-1-i] = 1
            L -= 1
            right -= 1        
        
    return "".join([str(a) for a in r[0]]) +","+ "".join([str(a) for a in r[1]])

print(solution(3,2,[2, 1, 1, 0, 1]))