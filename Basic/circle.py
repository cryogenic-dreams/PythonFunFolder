"""
This program makes a circle with the symbol you want.
@type ratio: integer
@param ratio: ratio > 0
"""
repeat = "y"
while repeat == "y":
    ratio = int(raw_input("Give me a ratio: "))
    symbol = raw_input("Give me the symbol to print: ")
    x = - ratio
    y = ratio
    while y >= - ratio:
        while x <= ratio:
            if (x*x + y*y) <= ratio*ratio:
                print symbol ,
            else:
                print " " ,
            x = x + 1
        print ""
        x = - ratio
        y = y - 1
    repeat = raw_input("Again? (y/n): ")

answer = raw_input("Did you liked it? (y/n): ")
if answer == "y":
    print "Thank you! (^_^)"
else:
    print "(>_<)"
