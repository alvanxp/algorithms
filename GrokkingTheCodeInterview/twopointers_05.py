def triplet_sum_close_to_target(arr, target_sum):
  right = len(arr)-1
  result = 0
  for idx in range(len(arr)-2):
      left = idx +1
      while idx < left and left < right:
          curr_sum = arr[idx] + arr[left] + arr[right]
          if curr_sum == target_sum:
              return target_sum
          if arr[left] < arr[right]:
              left += 1
          else:
              right -= 1
          if target_sum - result > target_sum - curr_sum  and target_sum - curr_sum >= 0 :
              result = curr_sum

  return result

print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))#1
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))#0
print(triplet_sum_close_to_target([1, 0, 1, 1], 100))#3