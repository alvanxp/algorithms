def find_permutation(str, pattern):
  windowStart = 0
  pattern_table = set()
  k = len(pattern)
  permutations = 0
  for w in pattern:
      pattern_table.add(w)
  for windowEnd in range(len(str)):
      right_letter = str[windowEnd]
      if right_letter not in pattern_table:
          windowStart += 1
          if permutations > 0:
              permutations -=1
      else:
          permutations += 1

      if permutations == k : return True

  return False
print(find_permutation("axacb", "abca"))  
# print(find_permutation("oidbcaf", "abc"))
# print(find_permutation("bcdxabcdy", "bcdyabcdx"))
# print(find_permutation("aaacb", "abc"))
# print(find_permutation("odicf", "dc"))