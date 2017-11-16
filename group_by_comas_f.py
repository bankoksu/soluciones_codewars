#group_by_comas
def group_by_commas(n):
    n1 = str(n)
    rango = len(n1)
    if rango <= 3:
        return n1
    if rango <= 6:
        return n1[-3:-1]+','+n1[-6:-4]
        
print (group_by_commas(100))
print (group_by_commas(1000))
print (group_by_commas(10000))
print (group_by_commas(100000))

def group_by_commas(n):
    n1 = (str(n))[::-1]
    rango = len(n1)
    position=0
    final_number = ""
    for number in n1:
        if position%3 ==0 and position != 0:
            final_number = final_number+ ','+ number
            position += 1
        else:    
            final_number = final_number + number
            position += 1
        
    return (final_number)[::-1]
        
print (group_by_commas(100))
print (group_by_commas(1000))
print (group_by_commas(10000))
print (group_by_commas(100000))
print (group_by_commas(52353458))"85435325"