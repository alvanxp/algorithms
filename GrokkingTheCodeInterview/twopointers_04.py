def search_triplets(arr):
  triplets = []
  arr.sort()
  print(arr)
  for idx in range(len(arr)):
      get_sum(arr, idx, triplets)
  return triplets

def get_sum(arr, idx, triplets):
    result = []
    left, right = idx+1, len(arr)-1
    h = set()
    while right > left:
        if arr[idx] + arr[left] + arr[right] == 0 :
            if str(arr[idx]) + str(arr[left])+ str(arr[right]) not in h:
                triplets.append([arr[idx] , arr[left] , arr[right]])
                h.add  cccccccccccccccccccccccccccccccccccccccc8x  dd             hj v ([arr[idx] , arr[left] , arr[right]])
        if  arr[idx] + arr[left] + arr[right] > 0:
bn 0     vvvb            right -= 1
        else:
            left += 1 
print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))