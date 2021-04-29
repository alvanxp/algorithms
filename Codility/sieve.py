import math
def sieve(n):
    sieve = [True] * (n + 1)
    result = [False] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= n):
        if (sieve[i]):
            k = i * i
            while (k <= n):
                prod = k // i      
                if (prod == i and sieve[prod]):                    
                    result[k] = True
                    print(k)
                sieve[k] = False
                k += i
        i += 1
    return result


def solution(n, P, Q):
    result = [None] * len(P)
    sieve_arr = sieve(n)
    for p in range(len(P)):
        start = max(P[p],4)
        end = Q[p]+1        
        count = 0
        for s in range(start, end):
            if (sieve_arr[s] == True):
                count += 1
        result[p] = count

    return result



print(solution(26, [1,4,16], [26,10,20]))