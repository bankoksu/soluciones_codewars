def getCount(inputStr):
    num_vowels = 0
    print (inputStr)
    vowels = "aeiouAEIOU"
    for letra in inputStr:
        if letra in vowels:
            num_vowels += 1
        else:
            pass
    
    return num_vowels
    
print (getCount('aladin'))
print (getCount('paladin'))
print (getCount('ghjtyl'))
print (getCount('abracadabra'))