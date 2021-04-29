def solution(S):
    if len(S) == 0: return 0
    if len(S) % 2 == 0: return 0
    middle = len(S) // 2
    for index in range(middle):
        if S[index] != S[len(S)-index-1]:
            return 0
    return middle