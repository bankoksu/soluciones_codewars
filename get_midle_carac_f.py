def get_middle(s):
    caracters = len(s)
    position = int(caracters/2)
    position1= int((caracters/2)+0.5)
    if caracters%2 == 0:
        return s[position-1]+s[position]
    elif caracters%2 != 0:
        return s[position1]