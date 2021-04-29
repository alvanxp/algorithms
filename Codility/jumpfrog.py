import math
def solution(X, Y, D):
    return math.ceil((Y - X) / D)

print(solution(0, 90, 30))