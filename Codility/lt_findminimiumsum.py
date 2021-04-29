def find_min_subarray_sum(A):
    if not A:
        return 0    
    stack = [[float('-inf'), -1, 0]] # value, index, accumulated_sum
    ans = 0
    for current_index, current_value in  enumerate(A):
        while stack and stack[-1][0] > current_value:
            stack.pop()
        stack_total = stack[-1][2]
        stack_index = stack[-1][1]
        total = (stack_total + (current_index - stack_index) * current_value)
        stack.append([current_value, current_index, total])
        ans = (ans + total)
    
    return int(ans % (10**9 + 7))

print(find_min_subarray_sum([3,1,2,4])) #17
print(find_min_subarray_sum([59,91])) #209
print(find_min_subarray_sum([62,92,97])) #467
