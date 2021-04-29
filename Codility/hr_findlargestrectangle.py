import sys
def findlargestrectanble(h):
    max_area = 0
    n = len(h)
    stack=[]
    for idx in range(n):
        max_area = max(max_area, h[idx])
        i= idx
        while len(stack) > 0 and stack[-1][0] >= h[idx] :
             prev = stack.pop()
             max_area = max(max_area, h[idx] * (idx +1- prev[1]))
             max_area = max(max_area, prev[0] * (idx - prev[1]))
             i = prev[1]
        else:
            stack.append((h[idx],i ))

    for idx in range(len(stack)):
        max_area= max(stack[idx][0] * (n-stack[idx][1]), max_area)
    
    return max_area


#print(findlargestrectanble([9,1,2,3,4,2,1])) #9
# print(findlargestrectanble([1,2,3,4,5])) #9
#print(findlargestrectanble([1,2,3,2,4])) #8
#print(findlargestrectanble([6320, 6020, 6098, 1332, 7263, 672, 9472, 2838, 3401, 9494]))
#print(findlargestrectanble([1,2,3,4,5])) #8
print(findlargestrectanble([8979, 4570 ,6436 ,5083 ,7780, 3269 ,5400 ,7579 ,2324 ,2116])) #26152