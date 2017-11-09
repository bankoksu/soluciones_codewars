def price(discont, sale):
    precioOriginal = (discont *100)/(100-sale)
    return round(precioOriginal,2)
    
print (price(75,25))
print (price(25,75))
print (price(75.75,25))
print (price(373.85,11.2))
print (price(458.2,17.13))
#print (price())