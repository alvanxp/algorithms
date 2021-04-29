def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = -1
  result = 0
  for idx in range(len(arr)-2):
      left = idx +1
      right = len(arr)-1
      while idx < left and left < right and right < len(arr):
          curr_sum = arr[idx] + arr[left] + arr[right]
          if target - curr_sum > 0:
            result += right - left
            left += 1 
          elif arr[left] < arr[right]:
              right -= 1
          else:
              left += 1
  return result
print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))#2
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))#4