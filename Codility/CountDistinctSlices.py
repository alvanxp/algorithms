def solution(M, A):    
    counter = 0
    n = len(A)
    front, current_value = 0 , 0
    if n == 1 : return 1
    for back in range(n):        
        if front == back:            
            current_value = A[front]            
            front += 1
            counter += 1
        while  (front < n and A[front] != current_value):
            current_value = A[front] 
            front += 1
            counter += 1       

        if front > n:            
            return counter
        elif front == n-1:  
            if current_value != A[front -1]:          
                counter += 1
            else:
                counter -= 1
            return counter
        if A[front] == current_value:
            front = back + 1
    return counter

def solution3(M, A):
    the_sum = 0
    front = back = 0
    seen = [False] * (M+1)
    while (front < len(A) and back < len(A)):
        while (front < len(A) and seen[A[front]] != True):
            the_sum += (front-back+1)
            seen[A[front]] = True
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen[A[back]] = False
                back += 1
                 
            seen[A[back]] = False
            back += 1
             
                 
    return min(the_sum, 1000000000)  

def solution2(M, A):
    m = [False] * (M + 1)
    front, back = 0, 0
    sum = 0
    n = len(A)
    while back < n and front < n:
        while front < n and m[A[front]] == False:
            sum += (front-back + 1)
            m[A[front]] = True
            front += 1
        else:
            while front < n and back < n and A[front] != A[back]:
                m[A[back]] = False
                back += 1
            m[A[back]] = False
            back += 1
    return sum

    
    
print(solution3(100000, [1, 1]))
#print(solution(0, [0]))
# print(solution(3, [1,2]))
# print(solution(1, [1]))
#print(solution2(6, [3, 4, 5, 5, 2]))