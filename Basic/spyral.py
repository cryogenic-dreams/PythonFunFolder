"""
This program reads a matrix doing spyrals. 
"""
def right_down (matrix, rowsup, rowinf, colleft, colright):
    """
    This program reads a matrix from left to right and from up to down.
    @type matrix: list of lists 
    @param matrix: a n x m matrix
    @type rowsup: integer
    @param rowsup: rowsup >= 0
    @type rowinf: integer
    @param rowinf: rowinf < len(matrix)
    @type colleft: integer
    @param colleft: colleft >= 0
    @type colright: integer
    @param colright: colright < len(matrix)
    @rtype: list
    @return: print list 
    """
    j = colleft
    while j < colright:
        print matrix[rowsup][j] ,
        j = j + 1
    i = rowsup
    while i <= rowinf:
        print matrix[i][colright] ,
        i = i + 1


def left_up (matrix, rowsup, rowinf, colleft, colright):
    """
    This program reads a matrix from right to left and from down to up.
    """
    j = colright
    while j > colleft:
        print matrix[rowinf][j] ,
        j = j - 1
    i = rowinf
    while i >= rowsup:
        print matrix[i][colleft] ,
        i = i - 1


#This is the main program.

def spyral (matrix):
    """
    This program reads a matrix given doing spyrals.
    @type matrix: list of lists
    @param matrix: a n x m matrix
    @rtype: list
    @return: print matrix in spyral.
    """
    rowsup = 0
    rowinf = len(matrix) - 1
    colleft = 0
    colright = len(matrix[0]) - 1
    while rowinf >= rowsup and colright >= colleft:
        right_down (matrix, rowsup, rowinf, colleft, colright)
        rowsup = rowsup + 1
        colright = colright - 1
        if rowinf - rowsup != -1 and colright - colleft != -1:
            left_up (matrix, rowsup, rowinf, colleft, colright)
            rowinf = rowinf - 1
            colleft = colleft + 1
