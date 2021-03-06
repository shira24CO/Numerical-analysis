import math


def printmat(matrix):
    for i in matrix:
        for j in i:
            print(j, end="  ")
        print()
    print()
def multiplyMatrix(mat1,mat2):
    result = []
    for i in range(len(mat1)):
        list = []
        for j in range(len(mat1)):
            res = 0
            for k in range(len(mat1)):
                res += (mat1[i][k] * mat2[k][j])
            list.append(res)
        result.append(list)
    return result

#מטריצה כולל איבר b 
def solvLU(A):
    size = len(A)  # Give us total of lines
    # (1) Extract the b vector
    b = [0 for i in range(size)]
    for i in range(size):
        b[i] = A[i][size]
    print("b= ",b)

    # (2) Fill L matrix and its diagonal with 1
    Lmat = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        Lmat[i][i] = 1

    # (3) Fill U matrix
    Umat = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(0, size):
            Umat[i][j] = A[i][j]
#
    size = len(Umat)

#----------------------------------------------------
    # (4) Find both U and L matrices
    for i in range(0, size):  # for i in [0,1,2,..,n]
        # (4.1) Find the maximun value in a column in order to change lines

        maxElem = abs(Umat[i][i])  #5
        maxRow = i                 #0

        for k in range(i+1, size):  # Interacting over the next line
            if (abs(Umat[k][i]) > maxElem):
                maxElem = abs(Umat[k][i])  # Next line on the diagonal
                maxRow = k
        elem = [[0 for i in range(size)] for i in range(size)]
        for z in range(size):
            elem[z][z] = 1
        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, size):
            # Interacting column by column
            for k in range(i,size):
                tmp = elem[maxRow][k]
                elem[maxRow][k] = elem[i][k]
                elem[i][k] = tmp
        print("ELEM")
        printmat(elem)
        print("matrix")
        printmat(Umat)
        Umat = multiplyMatrix(elem, Umat)
        print("resalt")
        printmat(Umat)


        # (4.3) Subtract lines
        for k in range(i + 1, size):
            c = -Umat[k][i] / float(Umat[i][i])
            print("pivot" ,c)
            Lmat[k][i] = c  # (4.4) Store the multiplier
            elem[k][i] = c
            print("Elem")
            printmat(elem)
            print("matrix")
            printmat(Umat)
            print("result")
            print(multiplyMatrix(elem,Umat))
            #for j in range(i, size):
                #Umat[k][j] += c * Umat[i][j]  # Multiply with the pivot line and subtract
        # (4.5) Make the rows bellow this one zero in the current column
        #for k in range(i + 1, size):
            #Umat[k][i] = 0
'''
    size = len(ID)

    # (5) Perform substitutioan Ly=b
    y = [0 for i in range(size)]
    for i in range(0, size, 1):
        y[i] = b[i] / float(ID[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * ID[i][k]

    size = len(matrix)

    # (6) Perform substitution Ux=y
    x = [0 in range(size)]
    for i in range(size - 1, -1, -1):
        x[i] = y[i] / float(matrix[i][i])
        for k in range(i - 1, -1, -1):
            matrix[i] -= x[i] * matrix[i][k]'''

#    return x
A = [[1,2,3,0],[4,5,6,0],[7,8,8,0]]
solvLU(A)