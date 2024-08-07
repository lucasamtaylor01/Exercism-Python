def translate(text):
    vogais = 'aeiou'
    
    if text.startswith("ay") or text.startswith("xr") or text.startswith("yt") or text[0].lower() in vogais:
        return text + 'ay'
    elif text[0].lower() not in vogais:
        return rule_two_b(text)
    
        
def rule_two_b(text):
    new_text = ""
    for i in range(1, len(text)):
        new_text += text[i]
    
    return new_text + text[0] + "ay"

print(rule_two_b("pig"))