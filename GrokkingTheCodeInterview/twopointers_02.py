def remove_duplicates(arr):
  count = 0
  start, end = 0,0
  while end < len(arr):
      if arr[start] == arr[end] or start == end:
          end += 1
      else:
          count += 1
          start = end  

  return count + 1
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))