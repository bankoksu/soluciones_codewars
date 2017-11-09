def swap(st):
    aeiou=["aeiou"]
    final_string = ""
    for letra in st:
        if letra in aeiou:
            letra= letra.upper()
            final_string = final_string + letra
        else:
            final_string = final_string + letra
            
    return final_string        
print (swap('perro'))
print (swap('pajaritos volando a mi alrededor'))
print (swap('Francia'))
print (swap('ole tuuuu!!'))