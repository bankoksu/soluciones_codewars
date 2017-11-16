def to_camel_case(text):
    
    if text.find("_") == -1:
        text = text.split("-")
    else:
        text = text.split("_")
    new_text = ""
    position=0
    for word in text:
        if position > 0:
            word =word.capitalize()
        new_text += word 
        position += 1
    return new_text
    
print(to_camel_case(''))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))

#el primero pasa los primeros caso test el siguiente fueron pruebas a continuacion.

def to_camel_case(text):
    if text.find("_") != -1:
        text = text.split("_")
    if text.find("-") != -1:
        text = text.split("-")
    new_text = ""
    position=0
    for word in text:
        if position > 0:
            word =word.capitalize()
        new_text += word 
        position += 1
    return new_text