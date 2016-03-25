"""
This is the matrix practice. This program returns the addition of two matrix
4th of March, 2011
"""

def read_matrix (path):
    """
    This program reads a file.
    @type path: text file path
    @param path: n x m numbers
    @rtype: list
    @return: matrix made of list of lists.
    """
    origin = open (path)
    line = origin.readline()
    matrix = []
    while line != "":
        row = convert_to_list (line)
        matrix.append (row)
        line = origin.readline()
    origin.close()
    return matrix


def convert_to_list (line):
    """
    This program makes the rows of the matrix making lists of list.
    @type line: string
    @param line: m columns of the matrix
    @rtype: list
    @return: convert string into a list
    """
    line_list = line.split()
    i = 0
    row = []
    while i < len(line_list):
        number = float(line_list[i])
        row.append (number)
        i = i + 1
    return row


def print_matrix (matrix):
    """
    This program prints the matrix given.
    @type matrix: list of lists
    @param matrix: a matrix of size n x m
    @rtype: printed matrix
    @return: print matrix from a list of lists
    """
    for row in matrix:
        for cell in row:
            print ("%2.2f" % (cell)) ,
        print


def write_matrix (matrix, path):
    """
    This program writes the matrix given into a text file.
    @type matrix: list of lists
    @param matrix: n x m
    @type path: text file path
    @param path: empty or n x m numbers
    @rtype: text file
    @return: write in a new text file the matrix
    """
    destination = open(path, "w")
    string = convert_to_string(matrix)
    destination.write(string)
    destination.close()
    

def convert_to_string (matrix):
    """
    This program converts a list to a string.
    @type matrix: list of lists
    @param matrix: n x m
    @rtype: string
    @return: make a string from a list 
    """
    i = 0
    cont = 0
    string = ""
    while i < len(matrix):
        while cont < len(matrix[i]):
            string = string + str(matrix[i][cont]) + " "
            cont = cont + 1
        string = string + "\n"
        cont = 0
        i = i + 1
    return string


def add_matrix (matrix1, matrix2):
    """
    This program adds two matrix.
    In order to work well this program, input two same size matrix n x m. If you want to add two that have differerent sizes, please, fill the columns or the rows that miss with zeros.
    @type matrix1: list of list
    @param matrix1: n x m
    @type matrix2: list of lists
    @param matrix2: n x m
    @rtype: list of lists
    @return: matrix n x m
    """
    i = 0
    new_matrix = []
    while i < len(matrix1):
        new_row = add_rows(matrix1, matrix2, i)
        new_matrix.append(new_row)
        i = i + 1
    return new_matrix


def add_rows(matrix1, matrix2, i):
    """
    This program makes the rows of a new matrix that is the addition of the two before.
    @type matrix1: list of lists
    @param matrix1: n x m
    @type matrix2: list of lists
    @param matrix2: n x m
    @type i: integer
    @param i: i >= 0
    @rtype: list
    @return: list that is the add of the two before
    """
    cont = 0
    new_row = []
    while cont < len(matrix1[i]):
        new_cell = matrix1[i][cont] + matrix2[i][cont]
        new_row.append(new_cell)
        cont = cont + 1
    return new_row


def main():
    """
    This is the main program, which points to the other subprograms.
    """
    matrix_a = read_matrix("a.txt")
    print_matrix(matrix_a)
    print "-----------"
    matrix_b = read_matrix("b.txt")
    print_matrix(matrix_b)
    print "-----------"
    matrix_c = add_matrix(matrix_a, matrix_b)
    print_matrix(matrix_c)
    print "-----------"
    write_matrix(matrix_c,"c.txt")
    matrix_d = read_matrix("c.txt")
    print "-----------"
    print_matrix(matrix_d)


if __name__ == "__main__":
    main()
