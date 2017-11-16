palindrome
def palindrome(num):
    
    if num > 0:
        num1 = (str(num))[::-1]
        if int(num1) == num:
            return True
        else:
            return False
    
    
    else:
        return "Not valid"

def palindrome(num):
    try:
        if num > 0 and num == "":
    
            num1 = (str(num))[::-1]
            if int(num1) == num:
                return True
            else:
                return False
                
        except:
            pass
    
        else:
            return "Not valid"
    





print(palindrome("ACCDDCCA"))