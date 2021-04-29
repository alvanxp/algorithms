def longest_substring_with_k_distinct(str, k):
  h = {}
  max_len = 0
  windowStart, windowSum = 0,0
  for windowEnd in range(len(str)):
    if str[windowEnd] not in h or h[str[windowEnd]] == 0:
      h[str[windowEnd]] =1  
      windowSum += 1
    else:
      h[str[windowEnd]] +=1
    if windowSum > k:
      h[str[windowStart]] -=1
      max_len = max(max_len, windowEnd - windowStart)
      windowSum -= 1
      windowStart +=1
  return max_len
print(longest_substring_with_k_distinct('araaci', 2))
print(longest_substring_with_k_distinct('araaci', 1))
print(longest_substring_with_k_distinct('cbbebi', 3))