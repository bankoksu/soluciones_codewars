def is_prime(num):
    if num <= 0:
        return False
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if(num%i) == 0:
            return False
    return True
    
print (is_prime(-4))    
print (is_prime(0))
print (is_prime(1))
print (is_prime(2))
print (is_prime(3))
print (is_prime(4))
print (is_prime(5))
print (is_prime(6))
print (is_prime(19))
print (is_prime(25))
print (is_prime(29))
print (is_prime(50))