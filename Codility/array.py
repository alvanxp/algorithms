def solution(A):
    # write your code in Python 3.6
    sum = 0
    for a in A:
        sum ^= a
    return sum

print(solution([9, 3, 9, 3, 9, 8, 9]))