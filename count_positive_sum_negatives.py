def count_positives_sum_negatives(arr):
    max =len(arr)
    contpos= 0
    contneg= 0
    if max != 0:
        for num in arr :
            if num > 0:
                contpos =contpos + 1
        
            elif num < 0:
                contneg = contneg + num
        
            elif num == 0:
                contpos = contpos
                contneg = contneg
        
        
            
    
        return [contpos,contneg]
    else:
        return arr
print (count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print (count_positives_sum_negatives([]))
        