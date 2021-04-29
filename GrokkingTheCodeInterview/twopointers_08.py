def funWithAnagrams(A):
    result = []
    start, end = 0, 1
    while (start < end and end < len(A)):
        if Is_Anagram(A[start], A[end]) == False:
            result.append(A[start])
            if end == len(A)-1:
                result.append(A[end])
            start = end
        end += 1
    result.sort()
    return result


def Is_Anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    results = {}
    for idx in range(len(word1)):
        if word1[idx] not in results:
            results[word1[idx]] = 0
        results[word1[idx]] += 1

    for idx in range(len(word2)):
        if word2[idx] not in results:
            results[word2[idx]] = 0
        results[word2[idx]] -= 1

    for key in results:
        if results[key] != 0:
            return False
    return True


#print(funWithAnagrams(["code", "doce", "ecod", "framer", "frame"]))
print(funWithAnagrams(["code", "aaagmnrs", "anagrams", "doce"]))


# def dutch_flag_sort(arr):
#     left, right = 0, len(arr)-1
#     while left < right:
#         if arr[left] > arr[right]:
#             temp = arr[right]
#             arr[right] = arr[left]
#             arr[left] = temp
#             right -= 1
#         elif arr[right] - arr[left] == 1:
#             left += 1
#         else:
#             right -= 1
#     return arr


# print(dutch_flag_sort([1, 0, 2, 1, 0]))
# print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
