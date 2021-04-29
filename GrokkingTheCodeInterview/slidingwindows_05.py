def fruits_into_baskets(fruits):
  h = {}
  max_fruits= 0
  windowStart, countFruitType = 0,0
  for windowEnd in range(len(fruits)):
    if fruits[windowEnd] not in h or h[fruits[windowEnd]] == 0:
      h[fruits[windowEnd]] =1       
      countFruitType += 1 
    else:
      h[fruits[windowEnd]] +=1
      
    if countFruitType > 2:
      h[fruits[windowStart]] -=1      
      countFruitType -= 1
      windowStart +=1
    max_fruits = max(max_fruits, (windowEnd - windowStart) +1)
  return max_fruits
print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C', 'C']))