import sys
# def max_slice_sum(A):
#     max_ending = 0
#     max_slice =  -sys.maxsize -1
#     for a in A:
#         max_ending = max(-sys.maxsize -1, max_ending + a)
#         max_ending = max(max_ending, a)
#         max_slice = max(max_slice, max_ending)
#     return max_slice

def max_slice_sum(A):
    slice = [sys.maxsize * -1] * (len(A)+1)
    suffix = [sys.maxsize * -1] * (len(A)+1)
    for i in range(len(A)):
        suffix[i+1] = max(max(0, suffix[i]) + A[i], A[i])        
        slice[i+1] = max(suffix[i+1], slice[i])
    return slice[-1]

#print(max_slice_sum([-2, 1])) #should be 1
#print(max_slice_sum([1,1, 1])) #should be 3
print(max_slice_sum([3,2,-6,4,0])) #should be 5
#print(max_slice_sum([-1000,-100,-50])) #should be -50
