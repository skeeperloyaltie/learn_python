import random

def nb_year(p0, percent, aug, p):
    year = 0
    if p > p0:
        p0 += p0 + (p0*percent/100) + aug 
        year += year
        return nb_year(p0, p, aug, percent)
        
    return year


print(nb_year(random.randint(12000, 13000), 2, random.randint(1000, 2000), random.randint(12000, 14000)))
        