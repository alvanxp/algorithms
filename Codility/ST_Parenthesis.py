def solution(S):
    result = 1
    stack = []
    for parenthesis in S:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        else:
            result = 0
    if len(stack) > 0:
        result = 0
    return result
print(solution("(())"))
print(solution("())"))
print(solution("(()(())())"))
print(solution("((("))
print(solution(")))"))