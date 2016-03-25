
def zero_matrix (rows):
    columns = rows + 1
    matrix = []
    for i in range (rows):
        matrix.append ([0] * columns)
    return matrix
    
def print_matrix (matrix):
    for i in range (len(matrix)):#desde el primero hasta que acabe la lista
        for j in range(len(matrix[0])):
            print "%4d" %matrix[i][j], #deja cuatro espacios entre numero y numero
        print
        

#This is the main program.

def n_goro (rows):
    matrix = zero_matrix(rows)
    i = 0
    j = 0
    for k in range (1,(rows*(rows + 1) + 1)):
        if i == len(matrix):
            i = 0 
        elif j == len(matrix[0]):
            j = 0
        matrix [i][j] = k
        i = i + 1
        j = j + 1
    print_matrix(matrix)
    print
    return matrix
