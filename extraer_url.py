def domain_name(url):
    parts = url.partition(".com")
    part1 = parts[0].partition("://")
    if part1[2][0] == "w":
        part2= part1[2].partition("www.")
        return '"'+part2[2]+'"'
        
    
    return '"'+part1[2]+'"'





print (domain_name("http://github.com/carbonfive/raygun"))   
print (domain_name("http://www.zombie-bites.com"))
print (domain_name("https://www.cnet.com"))