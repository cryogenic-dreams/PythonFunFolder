def m_c_d (x,y):
    if x > y:
        r = y
        while r > 0:
            r = x % r
            x = x / r
        else:
            r = x
            while r > 0:
                r = y % r
                y = y / r
    return r
