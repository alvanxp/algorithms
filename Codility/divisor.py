import sys
import math
def divisor(n):
    if (n < 1): return 0
    i = 1
    result = 0
    while (i * i < n ):
        if (n % i == 0):
            result += 2
        i += 1
    if (i * i == n):
        result += 1
    return result

def counter_area(n):
    if (n < 1): return 0
    i = 1
    multiplies = []
    perimeter= sys.maxsize
    while ( i * 2 <= n or i == n):
        if (n % i == 0):            
            if (len(multiplies) > 0 and multiplies[len(multiplies)-1] *i == n):
                a = multiplies.pop()
                b = i
                perimeter = get_perimeter(a, b, perimeter)
            else:
                multiplies.append(i)
        i += 1
    if (len(multiplies) > 0 and multiplies[len(multiplies)-1] *n == n):
        perimeter = get_perimeter( multiplies[len(multiplies)-1], n, perimeter)    
    return perimeter

def get_min_perimeter(N):
    if N <= 0:
      return 0
    sqrt_n = int(math.sqrt(N))
    for i in range(sqrt_n, 0, -1):
        if N % i == 0:
            return int(2*(i+N/i))
             
    raise Exception("should never reach here!") 

def get_perimeter(a, b, perimeter):
    perimeter = min(perimeter, (a + b) * 2)
    return perimeter

def primarity(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return False
        i += 1
    return True

print(get_min_perimeter(30))
#print(primarity(7))
#print(divisor(2147483647))