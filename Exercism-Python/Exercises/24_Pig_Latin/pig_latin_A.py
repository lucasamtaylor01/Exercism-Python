vogais = 'aeiou'

def consoant_counter(text):
    counter=0
    for i in range(len(text)):
        if text[i] not in vogais and text[i] != 'y':
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

def rule_four(text):
    new_text = ""
    y_position = 0

    for i in range(len(text)):
        if text[i] == 'y':
            y_position = i

    if y_position == 0:
        for i in range(1, len(text)):
           new_text += text[i]
        return new_text + 'yay'
    else:
        if (consoant_counter(text) != y_position):
            return rule_two(text, consoant_counter(text)) 
        
        for i in range(y_position, len(text)):
            new_text += text[i]

        for i in range(y_position):
            new_text+=text[i]

    return new_text + 'ay'

def translate(text):
    if ' ' in text:
        translated_words = []
        for word in text.split():
            translated_words.append(translate(word))
        return ' '.join(translated_words)
    else:
        if text.startswith(("ay", "xr", "yt")) or text[0].lower() in vogais:
            return text + 'ay'
        
        if 'qu' in text:
            return rule_three(text) 
        
        if text[0].lower() not in vogais:
            if 'y' in text:
                return rule_four(text)
            else:
                return rule_two(text, consoant_counter(text))
        