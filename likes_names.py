def likes(names):
    is_name = len(names)
    person_total = is_name - 2
    others =str(person_total)
    likes = " likes this"
    if is_name == 0:
        return 'no one' + likes
    elif is_name == 1:
        return names[0] + likes
    elif is_name == 2:
        return names[0] + ' and ' + names[1] + likes 
    elif is_name == 3:
        return names[0] + ',' + names[1] + ' and ' + names[2] + likes
    elif is_name >= 4:
        return names[0] + ',' + names[1] + ' and ' + others +' others' + likes
print (likes([]))
print (likes(['peter']))
print (likes(['jacob','alex']))
print (likes(['max','john','mark']))
print (likes(['alex','jacob','mark','max']))