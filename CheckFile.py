# Python 3 program to find rank of a matrix
class rankMatrix(object):
    def __init__(self, Matrix):
        self.R = len(Matrix)
        self.C = len(Matrix[0])


    # Function for exchanging two rows of a matrix
    def swap(self, Matrix, row1, row2, col):
        for i in range(col):
            temp = Matrix[row1][i]
            Matrix[row1][i] = Matrix[row2][i]
            Matrix[row2][i] = temp

    # Function to Display a matrix
    def Display(self, Matrix, row, col):
        for i in range(row):
            for j in range(col):
                print("aaa " + str(Matrix[i][j]))
            print('\n')

    @staticmethod
    def create_I_matrix(size,elementary_value,row,column):
        matrixI = []
        for i in range(size):
            matrixI_helper = []
            for j in range(size):
                if i == j:
                    matrixI_helper.append(1)
                else:
                    matrixI_helper.append(0)
            matrixI.append(matrixI_helper)
        matrixI[row][column] = elementary_value
        matrix = rankMatrix(matrixI)
        matrix.Display(matrixI,matrix.R,matrix.C)


    # Find rank of a matrix
    def rankOfMatrix(self, Matrix):
        rank = self.C
        for row in range(0, rank, 1):      # for i in range(2,10,3) ---> 2,5,8

            # Before we visit current row
            # 'row', we make sure that
            # mat[row][0],....mat[row][row-1]
            # are 0.

            # Diagonal element is not zero
            if Matrix[row][row] != 0:
                for col in range(0, self.R, 1):
                    if col != row:

                        # This makes all entries of current
                        # column as 0 except entry 'mat[row][row]'
                        multiplier = (Matrix[col][row] /
                                      Matrix[row][row])
                        print(self.create_I_matrix(self.R, multiplier, row, col))
                        print(multiplier)
                        for i in range(rank):
                            Matrix[col][i] -= (multiplier *
                                               Matrix[row][i])
                        #print(self.create_I_matrix(self.R, multiplier, row, col))

            # Diagonal element is already zero.
            # Two cases arise:
            # 1) If there is a row below it
            # with non-zero entry, then swap
            # this row with that row and process
            # that row
            # 2) If all elements in current
            # column below mat[r][row] are 0,
            # then remove this column by
            # swapping it with last column and
            # reducing number of columns by 1.
            else:
                reduce = True

                # Find the non-zero element
                # in current column
                for i in range(row + 1, self.R, 1):

                    # Swap the row with non-zero
                    # element with this row.
                    if Matrix[i][row] != 0:
                        self.swap(Matrix, row, i, rank)
                        reduce = False
                        break

                # If we did not find any row with
                # non-zero element in current
                # column, then all values in
                # this column are 0.
                if reduce:

                    # Reduce number of columns
                    rank -= 1

                    # copy the last column here
                    for i in range(0, self.R, 1):
                        Matrix[i][row] = Matrix[i][rank]
                        print(i,"abcderf")
                # process this row again
                row -= 1
        #print(self.create_I_matrix(self.R, multiplier, row, col))

        print(self.Display(Matrix, self.R,self.C))
        return (rank)

def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * determinant(m, sign * matrix[0][i])
    return answer

# Driver Code
if __name__ == '__main__':
    Matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 8]]
    RankMatrix = rankMatrix(Matrix)
    if determinant(Matrix, 1) != 0:
        print("Rank of the Matrix is:",
              (RankMatrix.rankOfMatrix(Matrix)))
    else:
        print("The matrix not invertable")




# This code is contributed by Vikas Chitturi
    '''[[1,0,0],
       [0,-3,0],
       [0,0,-1]]'''


