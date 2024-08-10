vogais = 'aeiou'

def consoant_counter(text):
    counter=0
    for i in range(len(text)):
        if text[i] not in vogais:
            counter+=1
        else:
            break
    return counter

def rule_two(text, n):
    new_text = ""
    for i in range(n, len(text)):
        new_text += text[i]
    
    for i in range(n):
        new_text += text[i]
    return new_text + "ay"

def rule_three(text):
    new_text = ""
    if text.startswith(("qu")):
        for i in range(2, len(text)):
            new_text += text[i]
        new_text += "quay"

    else:
        for i in range(3, len(text)):
            new_text += text[i]

        for i in range(3):
            new_text+= text[i]

        new_text+= "ay" 
    return new_text

def translate(text):
    
    if text.startswith(("ay", "xr", "yt")) or text[0].lower() in vogais:
        return text + 'ay'
    
    if 'qu' in text:
        return rule_three(text) 

    if text[0].lower() not in vogais:
        return rule_two(text, consoant_counter(text))
    
