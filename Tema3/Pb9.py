def args(*pos, **key):
    
    ct = 0
    for i in pos:
            if i in key.values():
                ct += 1
    return ct  

print(args(1, 2, 3, 4, a=1, b=2, c=3, d=5))