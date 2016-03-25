from math import sqrt
def triangle_number (position, row):
    """
    @type position: integer
    @param position: row>=position>=1
    @type row: integer
    @param row: row>0
    @rtype: integer
    @rparam: number>0
    """
    number = (row*(row - 1))/2 + position
    return number

    
def triangle_row (number):
    """
    @type number: integer
    @param number: number>0
    """
    number1 = int(sqrt(2*number))
    row = number1
    if row*(row + 1) < 2*number:
        row = number1 + 1
    return row
    

def same_row (number1, number2):
    """
    @type number1: integer
    @param number1: number1>0
    @type number2: integer
    @param number2: number2>0
    @rtype: boolean
    """
    return triangle_row (number1) == triangle_row (number2)

def triangle_column (number):
    """
    @type number: integer
    @param number: number>0
    """
    row = triangle_row (number)
    return number - (row * (row - 1))/2

def same_diagonal (number1, number2):
    """
    @type number1: integer
    @param number1: number1>0
    @type number2: integer
    @param number2: number2>0
    @rtype: boolean
    """
    return triangle_row (number1) - triangle_row (number2) == triangle_column (number1) - triangle_column (number2)
    
