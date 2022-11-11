f = "5, 6, 7"
# strip by comma and whitespace
g = [d.strip() for d in f.split(',') ]

print(g)
for d in g:
    if d > d:
        print(d * d)
    elif d[0] < d[2]:
        print(d[1] * d[2])
        
    else:
        print([d[0] * d[1] * d[2]])
        
    
    
    