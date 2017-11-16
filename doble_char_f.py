def double_char(s):
    max = len(s)
    finalchar = ""
    position = 0
    while position < max:
        finalchar = finalchar +(s[position]) *2
        position =position + 1
    if max == position:
        return finalchar
