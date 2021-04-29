def find_string_anagrams(str, pattern):
  result_indexes = []
  windowStart = 0
  pattern_table = {}
  k = len(pattern)
  permutations = 0
  for char in pattern:
      if char not in pattern_table:
          pattern_table[char] = 0
      pattern_table[char] = 1

  for windowEnd in range(len(str)):
      right_char = str[windowEnd]
      if right_char in pattern_table:
          if pattern_table[right_char] == 1:            
            pattern_table[right_char] -= 1
            permutations += 1
      if permutations == k:
        for idx in range(windowStart, windowEnd+1):
            result_indexes.append(idx)
        return result_indexes
      if windowEnd - windowStart + 1 - permutations > 0:
        for idx in range(windowStart, windowEnd):
            pattern_table[str[idx]] = 1 
        pattern_table[str[windowEnd]] = 0    
        windowStart = windowEnd
        permutations = 1
  return result_indexes

print(find_string_anagrams("ppqp", "pq")) #1,2
print(find_string_anagrams("abbcabc", "abc")) #2,3,4
print(find_string_anagrams("caacabc", "cba")) #4,5,6