def funWithAnagrams(arr):
    h = set()
    result = []
    for word in arr:
        arrWord = list(word)
        arrWord.sort()
        hashcode = "".join(arrWord)
        if hashcode not in h:
            result.append(word)
            h.add(hashcode)
    result.sort()
    return result
    
print(funWithAnagrams(['code', 'doce', 'ecod', 'framer', 'frame']))