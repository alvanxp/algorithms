def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  start, end = 0, len(arr) -1

  while end>start:
    current_sum = arr[end] + arr[start]
    if current_sum == target_sum:      
      return [start, end]
    if target_sum > current_sum:
        start +=1
    else: 
        end -= 1
    
  return [start, end]

print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))