for a in range(1,20):
    for b in range(1,32):
        for c in range(1,99):
            if a+b+c!=100:
                 continue
            if 5*a+3*b+c/3!=100:
                continue
            print(a,b,c)
