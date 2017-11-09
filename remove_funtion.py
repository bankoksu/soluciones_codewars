def remove(s):
    
signo = ('!')
    
palabra = s[-1:]
    
if palabra == signo:
        
return s[0:-1]
    
    
else:
        return s
    
   
        
        




print (remove("hi!"))

print (remove("hi"))

print (remove("hi! hi!"))

print (remove("!hi!"))