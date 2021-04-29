class Fish:
    def __init__(self, direction, size):
        self.direction = direction
        self.size = size

def solution(A, B):
    n = len(A)
    stack = []
    for i in range(n):
        if B[i] == 0:
            if len(stack) > 0 and stack[len(stack)-1].direction == 0 or len(stack) == 0:
                stack.append(Fish(B[i], A[i]))
            else:
                toAppend = True
                while len(stack) > 0 and stack[len(stack)-1].direction == 1:
                    if A[i] > stack[len(stack)-1].size:
                        stack.pop()
                    else:
                        toAppend = False 
                        break
                if toAppend:
                    stack.append(Fish(B[i], A[i]))
        else:
            stack.append(Fish(B[i], A[i]))
    return len(stack)

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
#print(solution([1, 3, 4, 5, 7], [0, 1, 1, 0, 1]))
            
            
        
        
  