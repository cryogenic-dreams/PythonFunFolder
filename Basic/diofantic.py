def diof (n):
    if n <=0 :
        print "There isn't solution"
    else:
        x = 0
        y = n
        t = (x,y)
        while  y > 0:
            x = x + 1
            y = y - 1
            t = t + (x,y)
    return t
