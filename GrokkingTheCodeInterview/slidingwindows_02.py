def max_sub_array_of_size_k(k, arr):
  result = -1000
  windowSum, windowStart = 0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= k - 1:
      result = max(windowSum, result)  # calculate the average
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead

  return result


print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))