def length_of_longest_substring(arr, k):
  windowStart = 0
  max_lenght = 0
  max_repeated_count = [0] * 2
  for windowEnd in range(len(arr)):
    max_repeated_count[arr[windowEnd]] +=1
    if windowEnd - windowStart + 1 - max_repeated_count[1] > k :
      max_repeated_count[arr[windowStart]] -= 1
      windowStart += 1
    else:
      max_lenght = max(max_lenght, windowEnd - windowStart + 1)
  return max_lenght
print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)) #6