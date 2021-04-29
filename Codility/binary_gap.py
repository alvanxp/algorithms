import sys
def solution(N):
    bin_string = format(N,"b")
    current = 0
    if (N < 1): return 0
    max_counter = 0
    isGap = False
    for i in range(len(bin_string)-1, -1, -1):
        b = bin_string[i]
        if (b == '1'):            
            if (not isGap):
                isGap = True                
            else:
                max_counter = max(current, max_counter)
                current=0
        else:
            if (isGap):
                current += 1
    return max_counter

print(solution( 1041 ))

