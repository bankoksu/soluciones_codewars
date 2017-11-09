def dashatize(num):
    num=str(abs(num))
    final_num = ""
    for number in num:
        if int(number)%2 ==0:
            final_num += number
        elif int(number)%2 != 0:
            final_num += "-"+number+"-"
            
    return final_num    
    
    
print(dashatize(274))
print(dashatize(-274))
print(dashatize(0))
print(dashatize(-248541))