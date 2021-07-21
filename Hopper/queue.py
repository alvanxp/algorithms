def isBalanced(s):
    stack = []
    for i in range(len(s)):        
        char = s[i]
        if len(stack) == 0:
            stack.append(s[i])
        else:
            stackchar = stack[-1]
            if char == ')' and stackchar == '(' or char == ']' and stackchar == '[' or char == '}' and stackchar == '{':                
                stack.pop()
            else:
                stack.append(s[i])
    
    return len(stack) == 0

print(isBalanced("{{[()]}}"))