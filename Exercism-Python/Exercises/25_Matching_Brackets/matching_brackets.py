def is_paired(input_string):
    # Verifica se os contadores estão corretos
    if counter_verifier(input_string):
        # Verifica se os fechamentos são válidos
        return is_valid_closure(input_string)
    else:
        return False

def counter_verifier(input_string):
    parenteses_counter = 0
    brackets_counter = 0
    braces_counter = 0
    
    for i in range(len(input_string)):
        if input_string[i] == '(' or input_string[i] == ')':
            parenteses_counter += 1
        elif input_string[i] == '{' or input_string[i] == '}':
            braces_counter += 1
        elif input_string[i] == '[' or input_string[i] == ']':
            brackets_counter += 1
    
    if parenteses_counter % 2 != 0 or braces_counter % 2 != 0 or brackets_counter % 2 != 0:
        return False
    else:
        return True

def is_valid_closure(input_string):
    for i in range(len(input_string)):
        if input_string[i] == '(':
            if not parenteses_verify(input_string, i):
                return False
        elif input_string[i] == '{':
            if not braces_verify(input_string, i):
                return False
        elif input_string[i] == '[':
            if not brackets_verify(input_string, i):
                return False
        
    return True

def parenteses_verify(input_string, i):
    for j in range(i + 1, len(input_string)):
        if input_string[j] == ')':
            return True
        if input_string[j] == '}' or input_string[j] == ']':
            break
    return False

def brackets_verify(input_string, i):
    for j in range(i + 1, len(input_string)):
        if input_string[j] == ']':
            return True
        if input_string[j] == '}' or input_string[j] == ')':
            break
    return False

def braces_verify(input_string, i):
    for j in range(i + 1, len(input_string)):
        if input_string[j] == '}':
            return True
        if input_string[j] == ']' or input_string[j] == ')':
            break
    return False

# wrong