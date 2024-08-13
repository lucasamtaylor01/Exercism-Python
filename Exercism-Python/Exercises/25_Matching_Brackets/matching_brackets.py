def is_paired(input_string):
    brackets_counter = 0
    braces_counter = 0
    parentheses_counter = 0

    
    for i in range(len(input_string)):
        if input_string[i] == '[':
            brackets_counter+=3
        if input_string[i]== ']':
            brackets_counter-=3
        if input_string[i] == '{':
            braces_counter+=2
        if input_string[i]== '}':
            braces_counter-=2
        if input_string[i] == '(':
            parentheses_counter+=1
        if input_string[i]== ')':
            parentheses_counter-=1
        
        if parentheses_counter < 0 or braces_counter < 0 or brackets_counter < 0:
           return False
    
    if parentheses_counter != 0 or braces_counter != 0 or brackets_counter != 0:
        return False
    else:
        return True
