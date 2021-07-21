def anagram(s):
    if len(s) % 2 > 0:
        return -1
    mid = len(s) // 2
    leftcounter = {}
    for i in range(mid):
        if s[i] not in leftcounter:
            leftcounter[s[i]] = 0
        leftcounter[s[i]] = leftcounter[s[i]] + 1

    result = 0 
    for i in range(mid, len(s)):        
         if s[i] in leftcounter :
             if leftcounter[s[i]] > 0:
                leftcounter[s[i]] = leftcounter[s[i]] -1
    for key in leftcounter:
        if leftcounter[key] > 0:
            result += leftcounter[key]
    return result

print(anagram("aaabbb"))
print(anagram("ab"))
print(anagram("fdhlvosfpafhalll"))
print(anagram("xaxbbbxx"))