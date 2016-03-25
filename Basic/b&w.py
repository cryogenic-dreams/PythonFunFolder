def b_w (row):
    """
    This program makes a square with asterisks when you imput the row.
    If you want a 8*8 square, just imput 8.
    """
    i = 0
    while i < row:
        if i % 2 == 0:
            print " *" * row
        else: 
            print "* " * row
        i = i + 1
