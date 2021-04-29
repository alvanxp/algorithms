import math
def smallest_subarray_with_given_sum(K, arr):
  min_lenght = math.inf
  windowSum, windowStart = 0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    while windowSum >= K:
    #if windowSum >= K :
      min_lenght = min(min_lenght, windowEnd - windowStart+1)
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead
  if min_lenght == math.inf:
    return 0
  return min_lenght

#print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
#print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))