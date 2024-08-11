vogais = 'aeiou'

def consoant_counter(text):
    counter = 0
    for char in text:
        if char not in vogais and char != 'y':
            counter += 1
        else:
            break
    return counter

def rule_two(text, n):
    return text[n:] + text[:n] + "ay"

def rule_three(text):
    if text.startswith("qu"):
        return text[2:] + "quay"
    return text[3:] + text[:3] + "ay"

def rule_four(text):
    y_position = text.find('y')
    
    if y_position == -1:
        return rule_two(text, consoant_counter(text))

    if y_position == 0:
        return text[1:] + "yay"
    
    if consoant_counter(text) != y_position:
        return rule_two(text, consoant_counter(text))
    
    return text[y_position:] + text[:y_position] + 'ay'

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if word.startswith(("ay", "xr", "yt")) or word[0].lower() in vogais:
            translated_words.append(word + "ay")
        elif 'qu' in word:
            translated_words.append(rule_three(word))
        elif 'y' in word:
            translated_words.append(rule_four(word))
        else:
            translated_words.append(rule_two(word, consoant_counter(word)))

    return ' '.join(translated_words)
