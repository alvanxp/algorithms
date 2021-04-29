def solution(A):
    # write your code in Python 3.6
    result = [''] * len(A)
    hashtable = {}
    for idx in range(len(A)):
        if A[idx] not in hashtable:
            hashtable[A[idx]] = (1, idx)
        else:
            hashtable[A[idx]] = (hashtable[A[idx]][0] +
                                 1, hashtable[A[idx]][1])
    tupleList = []
    for tup in hashtable:
        tupleList.append(hashtable[tup])

    tupleList.sort(key=lambda tup: (-tup[0], tup[1]))
    idx = 0
    for item in tupleList:
        for i in range(idx, idx + item[0]):
            result[i] = str(A[item[1]])
        idx = i+1
    return result


print(solution([5, 5, 4, 6, 4]))
# print(solution([2, 5, 2, 8, 5, 6, 8, 8]))
# print(solution([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]))
