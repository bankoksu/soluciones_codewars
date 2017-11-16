def DNA_Strand(dna):
    final_dna= ""
    for valor in dna:
        if valor == "T":
            final_dna = final_dna + "A"
        
        elif valor == "A":
            final_dna = final_dna + "T"
            
        elif valor == "C":
            final_dna = final_dna + "G"
        
        elif valor == "G":
            final_dna = final_dna + "C"
    
    else:
        return final_dna
        
        
print (DNA_Strand("ATTGC"))
print (DNA_Strand("GTAT"))