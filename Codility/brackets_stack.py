def solution(S):
    stack = []
    for c in S:
        is_correct = True
        last_opened = ''
        if len(stack) > 0:
            last_opened = stack[len(stack)-1]
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        elif c == '}':
            is_correct = last_opened == '{'
            if is_correct:
                stack.pop()
        elif c == ']':
            is_correct = last_opened == '['
            if is_correct:
                stack.pop()
        elif c == ')':
            is_correct =  last_opened == '('
            if is_correct:
                stack.pop()
        if not is_correct:
            return False
    
    if len(stack) != 0 :
        return False
    return True
print(solution(")("))  #invalid
#print(solution("{}"))  #valid
#print(solution("{}[]()")) #valid
#print(solution("{[()]}")) #valid
#print(solution("{[(])]}")) #invalid
