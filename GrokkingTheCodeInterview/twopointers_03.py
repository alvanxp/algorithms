def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares



# def make_squares(arr):
#   squares = [0] * len(arr)
#   mid = len(arr) // 2
#   squares[0] = arr[mid]
#   result_idx = 1
#   for idx in range(mid+1, len(arr)):
#       right_square = arr[idx] * arr[idx]
#       left_square = arr[mid -(idx -mid)] * arr[mid -(idx -mid)]
#       if right_square > left_square:
#           squares[result_idx] = left_square
#           result_idx += 1
#           squares[result_idx] = right_square
#       elif right_square < left_square:
#           squares[result_idx] = right_square
#           result_idx += 1
#           squares[result_idx] = left_square
#       else:
#           squares[result_idx] = right_square
#           result_idx += 1
#           squares[result_idx] = left_square
#       result_idx += 1
#   return squares

         


print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))