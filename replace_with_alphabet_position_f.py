def alphabet_position(text):
    text = text.lower().replace(' ','')
    ascii_code = 96
    new_text =""
    for letra in text:
        letra =(ord(letra))
        letra = letra - ascii_code
        if letra > 0:
            letra =str(letra)
            new_text = new_text + letra + " "
        else:
            pass
    
    return new_text[:-1]