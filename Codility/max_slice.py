def solution(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

def solution2(A):    
    max_profit = 0
    max_day = 0
    min_day = 200000
     
    for day in A:
        min_day = min(min_day, day)
        max_profit = max(max_profit, day-min_day)
     
    return max_profit
#print(max_rest([7,3,5,6,4,8]))
print(solution2([4, 2, 1]))

print(solution2([23171, 21011, 21123, 21366, 21013, 21367]))

# print(solution([2, 1, 6, 4, 3, 7]))
# print(solution([2, 4, 1, 6, 5, 9, 7]))
# print(solution([4, 3, 2, 6, 1]))