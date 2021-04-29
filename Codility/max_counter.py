def solution2(N, A):    
    counters = [0] * N
    start_line = 0
    current_max = 0
    for i in A:
        x = i - 1
        if i > N:
            start_line = current_max
        elif counters[x] < start_line: 
            counters[x] = start_line + 1
        else:
            counters[x] += 1
        if i <= N and counters[x] > current_max:
            current_max = counters[x]
    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line
    return counters
        

def solution(N, A):    
    current_max_counter = 0
    max_idx = 0
    result = [0] * (N)     
    max_counter = 0 
    for i in range(len(A)):
        if (A[i] > N ):
            max_idx = i #rellenar todo
            max_counter = current_max_counter
            current_max_counter = 0
        else:
            result[A[i]-1] += 1
            current_max_counter = max(result[A[i]-1], current_max_counter)    
     
    if max_counter > 0:
        for i in range(0, N):
            result[i] = max_counter

        for i in range(max_idx+1, len(A)):
            result[A[i]-1] += 1
    return result

#print(solution(5, [3, 4, 4, 4, 4, 4, 6]))
#print(solution(1, [1]))
print(solution2(5, [3, 4, 4, 6, 1, 4, 4]))