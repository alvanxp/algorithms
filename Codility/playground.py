import sys
from collections import deque
def matchingStrings(strings, queries):
    h = [0] * len(queries)
    dic = {}
    for s in strings: 
        if s in dic:
            dic[s] += 1
        else:           
            dic[s] = 1 
    for q in range(len(queries)):
        if queries[q] in dic:
            h[q] = dic[queries[q]]
    return h

class Rectangle:
    def __init__(self, value, index):
        self.value = value
        self.index = index
    
def largestRectangle(histogram):    
    index = 0
    left_index = 0
    s = []
    max_area = 0
    while index < len(histogram):
        if not s or histogram[s[-1]] <= histogram[index]:
            s.append(index)
            index += 1
        else:            
            left_index = s.pop()
            if s:
                positions = (index - s[-1]-1 )
                area = histogram[left_index] * positions 
                print(" left_index: "+str(left_index)+" index: "+str(index)+" positions: "+str(positions)+ " value:"+str(histogram[left_index])+ " new area:" +str(area))
                max_area = max(max_area, area)
            else:
                positions = (index)
                area = histogram[left_index] * positions 
                print(" left_index: "+str(left_index)+" index: "+str(index)+" positions: "+str(positions)+ " value:"+str(histogram[left_index])+ " new area:" +str(area))
                max_area = max(max_area, area )

    while s:
        left_index = s.pop()
        if s:
            positions = (index - s[-1]-1 )
            area = histogram[left_index] * positions 
            print(" left_index: "+str(left_index)+" index: "+str(index)+" positions: "+str(positions)+ " value:"+str(histogram[left_index])+ " new area:" +str(area))
            max_area = max(max_area, area)
        else:
            positions = (index)
            area = histogram[left_index] * positions 
            print(" left_index: "+str(left_index)+" index: "+str(index)+" positions: "+str(positions)+ " value:"+str(histogram[left_index])+ " new area:" +str(area))
            max_area = max(max_area, area )



    return max_area

def count_triangles(A):
    A.sort()
    count  = 0
    n = len(A)
    for P in range(n-2):        
        for Q in range(P + 1, n):
            R = Q + 1
            while R < n and A[P]+ A[Q] > A[R]:
                R +=1  
            if R == n:
                count += R - Q -1          

    return count

def greddyCoinChanging(M, k):
    n = len(M)
    result = []
    for i in range(n-1, -1,-1):
        result += [(M[i], k // M[i])]
        k %= M[i]
    return result

def greedyCanoeist(W, k):
    N = len(W)
    skinny = deque()
    fatso= deque()
    for i in range(N -1):
        if W[i] + W[-1] <= k :
            skinny.append(W[i])
        else:
            fatso.append(W[i])
    fatso.append(W[-1])
    canoes = 0
    while skinny or fatso:
        if len(skinny) > 0:
            skinny.pop()
        fatso.pop()
        canoes +=1
        if not fatso and skinny : 
            fatso.append(skinny.pop())
        while len(fatso) > 1 and fatso[-1]:
            skinny.append(fatso.popleft())
    return canoes


# def dynamic_coin_chanching(C, k):
#     n = len(C)
#     dp = [[0] * (k + 1) for i in range(n+1)]
#     dp[0] = [0] + [sys.maxsize] * k
#     for i in range(1, n + 1):
#         for j in range(C[i-1]):
#             dp[i][j] = dp[i -1][j]
#         for j in range(C[i -1], k + 1):
#             dp[i][j] = min(dp[i][j-C[i -1]] + 1, dp[i-1][j])
#     return dp[n][k]

# print(dynamic_coin_chanching([1,3,4], 6))


def dynamic_coin_changing2(C, k):
    n = len(C)
    dp = [[0] * (k+1) for i in range(n+1)] 
    dp[0] = [0] + [sys.maxsize] * k
    for i in range(1,n + 1):
        for j in range(C[i -1]):
            dp[i][j] = dp[i-1][j]
        for j in range(C[i -1], k +1):
            dp[i][j] = min(dp[i][j-C[i-1]]+1, dp[i-1][j])
    return dp[n][k]

def dynamic_coin_changing3(C, k):
    n = len(C)
    dp = [0] + [sys.maxsize] * k
    for i in range(1, n+1):
        for j in range(C[i -1], k +1):
            dp[j] = min(dp[j - C[i-1]] + 1 , dp[j])
    return dp[k]

def max_sum(arr):
    n = len(arr)
    incl = arr[0]
    excl = 0
    excl_new =0
    for a in arr[1:]:
        excl_new = max(incl, excl)
        incl = excl + a
        excl = excl_new
    return max(incl, excl)
    
def dynamic_max_sum(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    ans = max(dp)
    for a in arr[2:]:
        max_algo = max(dp[-2]+a, a)
        dp.append(max(max_algo, ans))
        ans = max(ans, dp[-1])
    return ans	

def checkSubarraySum2(nums, k):
    if not k: k = 2**31
    d, s = set(), 0
    for n in nums:
        t = (n + s) % k
        s, s
        if s in d:
            return True
        d.add(t)
    return False


def checkSubarraySum(nums, k):
    if len(nums) == 1 or len(nums) == 0: return False
    sum_correlatives = 0
    alter_sum = nums[0]
    for i in range(1,len(nums)):
        sum_correlatives = nums[i] + nums[i-1]  
        if (k == 0 and sum_correlatives == 0): return True
        if (abs(k) > 0): 
            if sum_correlatives % abs(k) == 0:
                print(sum_correlatives)
                return True
        alter_sum+=nums[i]
    if k == 0 and alter_sum > 0 : return False
    return alter_sum % abs(k) == 0

def longestStrChain(words):
    listofchains = {}
    lastpredecesor = words[0]
    sortWords = []
    for w in words:
        sortWords.append(''.join(sorted(w)))
    sortWords.sort(key=len)
    for w in sortWords:        
        if w not in listofchains:
            listofchains[w] = []
            listofchains[w].append(w)
        else:
            for key in listofchains:
                if key in w and listofchains[key][-1] in w:                
                    listofchains[key].append(w) 

    maxchain = 0;
    for key in listofchains:
        maxchain= max(len(listofchains[key]), maxchain)
    return maxchain


def solution(A):
    max_sum = sys.maxsize * -1
    max_sum = max(max_sum, A[0])
    sum_slide = A[0]
    for i in range(1, len(A)):        
        sum_slide += A[i]
        sum_slide = max(sum_slide, A[i])
        max_sum = max(max_sum, sum_slide)
    return max_sum

def subarraySum(nums, k):
    if not list:
        return 0
    prefix_dict = {0:1}
    cur_sum = 0
    res = 0
    for n in nums:
        cur_sum += n
        lookfor = cur_sum - k
        if lookfor in prefix_dict:
            res += prefix_dict[lookfor]
        if cur_sum not in prefix_dict:
            prefix_dict[cur_sum] = 1
        else:
            prefix_dict[cur_sum] += 1
            
    return res

#print(subarraySum([1,2,3], 3)) #2
#print(subarraySum([0,0,0,0,0,0,0,0,0,0],0)) #2
# print(subarraySum([1,1,1], 2)) #2
print(subarraySum([1,2,2,1,1,2], 6)) #3
# print(solution([-2, 1, 1]))

# print(longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
#print(checkSubarraySum2([3,2,4,1,17],7))
#print(checkSubarraySum([470,161,377,184,118,91,413,73,224,167,505,413,521,5,7,372,393,523,211,479,90,516,238,467,410,51,337,31,442,297,100,75,260,33,490,477,21,374,233,41,215,87,84,153,271,241,169,275,323,358,291,176,423,426,296,175,413,423,387,416,27,266,257,136,27,155,77,142,60,335,401,443,52,153,345,71,117,443,177,238,433,464,323,79,156,429,79,327,64,335,92,147,350,480,277,335,97,317,420,453],75))
#print(max_sum([3,5,-7,8,10]))
#print(max_sum([5,7,4,6,5]))

# print(dynamic_max_sum([3,5,-7,8,10]))
# print(dynamic_max_sum([3,7,4,6,5]))
#print(dynamic_coin_changing2([1,3,4], 6))
#print(dynamic_coin_changing3([1,3,4], 6))

#print(greedyCanoeist([2,5,7,8,9, 12,14], 15))

#print(greddyCoinChanging([1,2], 5))


#print(count_triangles([10,2,5,1,8,12]))
        
    
#print(largestRectangle([2,1,4,3,3,2,4,1]))
#print(largestRectangle([8979, 4570, 6436, 5083 ,7780 ,3269 ,5400 ,7579, 2324, 2116]))
#print(matchingStrings(["de", "de"],["de"]))
