def capitals(word):
    lista = []
    position = 0
    for valor in word:
        es = valor.isupper()
        if es == True:
            lista.append(position)
            position += 1
            
            
        else:
            position += 1
            
            

    return lista