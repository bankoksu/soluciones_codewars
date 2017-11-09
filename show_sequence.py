def show_sequence(n):
    lista = list(range(n+1))
    total = 0
    lista_num=""
    if n > 0:
        for number in lista:
            total += number
            lista_num= lista_num + '+' + str(number)
        return (lista_num[1:] + ' = ' + str(total))   
    elif n == 0:
        return (str(total) + '=' + str(n))
    
    else:
        return (str(n) +"<0")