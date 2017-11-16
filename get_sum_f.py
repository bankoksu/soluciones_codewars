def get_sum(a,b):
    if a == 0:
        return b
        
    elif b == 0:
        return a
    
    elif a and b:
        if a < b :
            return b
        elif a > b:
            return a
    
    elif a == b :
        return 'since both are same'
            
        
print (get_sum(0,1))
print (get_sum(0,-1))    
print (get_sum(5,-2))
print (get_sum(-1,2))
print (get_sum(1,1))


def get_sum(a,b):
    if a == 0:
        return b    
        
    elif b == 0:
        return a
        
    elif a == b:
        return a ,'since both are same'
        
        
    elif a or b < 0: 
        if  a > 0 and b > 0:
            return (a+b)
        elif a < b:
            return b
        elif a > b:
            return a

            def get_sum(a,b):   
    if a == b:
        return a 
    
    elif  a >= 0 and b >= 0:
            return (a+b)     
    
    elif a or b < 0: 
        if a == 0 and b < 0:
            return b
        elif b == 0 and a <0:
            return a
        elif a < 0:
            return b
        elif b < 0:
            return a