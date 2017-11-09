def counter_effect(hit_count):
    numero = []
    final_list = []
    for number in hit_count:
        numero.append(int(number))
        
    for number in numero:
        numeritos = list(range(0,number+1))
        final_list.append(numeritos)
        
    return final_list    




print (counter_effect("1250"))
print (counter_effect("1000"))
print (counter_effect("0050"))
print (counter_effect("2501"))
print (counter_effect("0000"))