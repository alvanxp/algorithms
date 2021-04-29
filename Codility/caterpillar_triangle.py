def solution(A):
    P,Q,R = 0,1,2
    counter = 0
    n = len(A)
    if n < 3: return 0
    while R < n and Q < R and P < Q:
        while R < n and Q < R:
            if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
                counter += 1
            R += 1
        else:
            if R >= n:
                Q += 1
                R = Q +1
        if Q == n-1 and R == n:
            P+=1
            Q = P + 1
            R = Q + 1 

    return counter

def solution2(A):
    P,Q,R = 0,1,2
    A.sort()
    counter = 0
    n = len(A)
    if n < 3: return 0
    while R < n and Q < R and P < Q:
        while R < n and Q < R:
            if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
                counter += 1
                R += 1    
            else:
                Q += 1
                R = Q+1
            if R == n:
                Q += 1
                R = Q+1
        else:
            P+=1
            Q=P+1
            R =Q+1

    return counter

def solution3(A):
    A.sort()
    triangle_cnt = 0
     
    for P in range(0, len(A)-2):
        Q = P + 1
        R = P + 2
        while (R < len(A)):
            if A[P] + A[Q] > A[R]:
                triangle_cnt += R - Q
                R += 1
            elif Q < R -1:
                    Q += 1
            else:
                R += 1
                Q += 1
                 
    return triangle_cnt

print(solution3([10,2,5,1,8,12,14]))
#print(solution2([3, 3, 5, 6]))