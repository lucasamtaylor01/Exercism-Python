def is_paired(s):
    stack = []
    for i in range(len(s)): 
        if s[i] in "({[":
            stack.append(s[i])
        elif s[i] in ")}]":
            if not stack:
                return False
            current = stack.pop()
            if current == '[':
                if s[i] != ']':
                    return False
            elif current == '{':
                if s[i] != '}':
                    return False
            elif current == '(':
                if s[i] != ')':
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
    
