def non_repeat_substring(str):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str)):
    right_char = str[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[str[window_end]] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

# def non_repeat_substring(str):
#   h = {}
#   max_len = 0
#   windowStart, windowSum = 0,0
#   for windowEnd in range(len(str)):
#     if str[windowEnd] not in h or h[str[windowEnd]] == 0:
#       h[str[windowEnd]] =1      
#     else:
#       h[str[windowEnd]] +=1
#       windowSum += 1
#     if windowSum > 0:
#       h[str[windowStart]] -=1
#       max_len = max(max_len, windowEnd - windowStart)
#       windowSum -= 1
#       windowStart = windowEnd
#   return max_len

# print(non_repeat_substring("aabccbb"))
# print(non_repeat_substring("abbbb"))
print(non_repeat_substring("abccde"))