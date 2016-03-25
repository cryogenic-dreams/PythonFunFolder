def vulcano(row):
    """
    This program makes a vulcano with the rows you want. 
    But, since row = 8, you will need a bigger screen to see the vulcano."
    """
    n = 1
    while n < 2 ** row:
        print (((2 ** row) / 2) - n) * " " + "**" * n
        n = n * 2

        

