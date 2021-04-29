def caterpillar_method(A, s):
    n = len(A)
    front, total = 0 , 0
    for back in range(n):
        while  (front < n and total + A[front] <= s):
            total += A[front]
            front += 1
        if total == s:
            return True
        total -= A[back]
    return False

caterpillar_method([6,2,7,4,1,3,6], 12)