def product(s):
    interrogacion = 0
    exclamacion = 0
    for valor in s:
        if valor == '?':
            interrogacion = interrogacion + 1
        elif valor == '!':
            exclamacion = exclamacion +1
        else:
            continue
            
    return interrogacion * exclamacion