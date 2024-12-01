import random


class Service:
    def __init__(self, repo):
        self.__repo = repo

    def matrix(self):
        return self.__repo.get_matrix()


    def stars(self,matrix):
        """
        In this function we generate two random numbers between 1 and 8 that represent the coordinates ex:matrix[a][b].
        After the numbers are generated, we check wether there are any starst beside it in every direction, and we
        also have special cases for a=1,b=1, a and b =8,a and b =1,a=8 and b=8.
        If every condition is met,and if the location does not have a star already, we place the star in the matrix.
        We return the new matrix
        :param matrix: the matrix that is being recieved without stars
        :return: the same matrix but with now the added sars in it
        """
        k = 0
        while k<10:
            try:
                a = random.randint(1, 8)
                b = random.randint(1, 8)
                if matrix[a - 1][b - 1] == 0 and matrix[a][b - 1] == 0 and matrix[a - 1][b] == 0 and \
                        matrix[a + 1][b + 1] == 0 and matrix[a - 1][b + 1] == 0 and matrix[a][
                    b + 1] == 0 and \
                        matrix[a + 1][b] == 0 and matrix[a + 1][b - 1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k = k + 1
                elif a == 1 and matrix[a][b - 1] == 0 and matrix[a + 1][b + 1] == 0 and matrix[a][
                    b + 1] == 0 and \
                        matrix[a + 1][b] == 0 and matrix[a + 1][b - 1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k = k+1
                elif a == 8 and matrix[a][b - 1] == 0 and matrix[a -1][b + 1] == 0 and matrix[a][
                    b + 1] == 0 and \
                        matrix[a - 1][b] == 0 and matrix[a - 1][b - 1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k=k+1
                elif b == 8 and matrix[a - 1][b - 1] == 0 and matrix[a][b - 1] == 0 and matrix[a - 1][b] == 0 and \
                        matrix[a + 1][b] == 0 and matrix[a + 1][b - 1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k = k + 1
                elif b == 1 and matrix[a - 1][b + 1] == 0 and matrix[a][b + 1] == 0 and matrix[a - 1][b] == 0 and \
                        matrix[a + 1][b] == 0 and matrix[a + 1][b + 1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k = k + 1
                elif a == 1 and b == 1 and matrix[a+1][b] == 0 and matrix[a+1][b+1] == 0 and matrix[a][b+1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k = k + 1
                elif a == 8 and b == 8 and matrix[a - 1][b] == 0 and matrix[a - 1][b - 1] == 0 and matrix[a][
                        b - 1] == 0 and matrix[a][b]==0:
                    matrix[a][b] = '*'
                    k = k + 1
            except:
                pass
        return matrix

    def ship(self,matrix):
        k = 0
        while k < 1:
            a = random.randint(1, 8)
            b = random.randint(1, 8)
            try:
                if matrix[a][b] != '*':
                    matrix[a][b] = 'E'
                    k = 1
            except:
                pass
        return matrix


    def gen_blingon(self,matrix):
        k = 0
        while k<3:
            a=random.randint(1,8)
            b=random.randint(1,8)
            try:
                if matrix[a][b] == 0:
                    matrix[a][b] = 'B'
                    k+=1
            except:
                pass
        return matrix


    def wrap(self,i,j,matrixb):
        for li in range(len(matrixb)):
            for lj in range(len(matrixb[li])):
                if matrixb[li][lj] == 'E':
                    ie = li
                    ej = lj
        if i!=ie and j!=ej:
            return 'w'
        elif matrixb[i][j] == 'B':
            return 'o'
        elif matrixb[i][j] == 0:
            for li in range(len(matrixb)):
                for lj in range(len(matrixb[li])):
                    if matrixb[li][lj] == 'E':
                        matrixb[li][lj] = 0
            matrixb[i][j] = 'E'
            return matrixb[i][j]
        elif matrixb[i][j] == '*':
            return 's'


    def fire(self,i,j,matrixb):
        for li in range(len(matrixb)):
            for lj in range(len(matrixb[li])):
                if matrixb[li][lj] == 'E':
                    ie = li
                    ej = lj
        if matrixb[i][j] == 'B':
            matrixb[i][j] = 0
            return matrixb
        elif matrixb[i][j]=='*' or matrixb[i][j]==0:
            return'm'
        elif ie-i>1 or lj-j>1:
            return 'e'
        elif ie-li>1 or ej-j>1:
            return 'e'


    def check_b(self,matrix2,matrixb):
        for i in range(len(matrixb)):
            for j in range(len(matrixb[i])):
                if matrixb[i][j] == 'E':
                    if i ==1 and j ==1:
                        if matrixb[i+1][j+1] == 'B':
                            matrix2[i+1][j+1] = 'B'
                        elif matrixb[i][j+1] == 'B':
                            matrix2[i][j+1] = 'B'
                        elif matrixb[i+1][j] == 'B':
                            matrix2[i+1][j] = 'B'
                    elif i==8 and j==8:
                        if matrixb[i-1][j-1] == 'B':
                            matrix2[i-1][j-1] = 'B'
                        elif matrixb[i][j-1] == 'B':
                            matrix2[i][j-1] = 'B'
                        elif matrixb[i-1][j] == 'B':
                            matrix2[i-1][j] = 'B'
                    elif i == 1:
                        if matrixb[i + 1][j + 1] == 'B':
                            matrix2[i + 1][j + 1] = 'B'
                        elif matrixb[i][j + 1] == 'B':
                            matrix2[i][j + 1] = 'B'
                        elif matrixb[i + 1][j] == 'B':
                            matrix2[i + 1][j] = 'B'
                        elif matrixb[i + 1][j - 1] == 'B':
                            matrix2[i + 1][j - 1] = 'B'
                        elif matrixb[i][j - 1] == 'B':
                            matrix2[i][j - 1] = 'B'
                        elif matrixb[i + 1][j-1] == 'B':
                            matrix2[i + 1][j-1] = 'B'
                    elif i == 8:
                        if matrixb[i - 1][j + 1] == 'B':
                            matrix2[i - 1][j + 1] = 'B'
                        elif matrixb[i][j + 1] == 'B':
                            matrix2[i][j + 1] = 'B'
                        elif matrixb[i - 1][j] == 'B':
                            matrix2[i - 1][j] = 'B'
                        elif matrixb[i - 1][j - 1] == 'B':
                            matrix2[i - 1][j - 1] = 'B'
                        elif matrixb[i][j - 1] == 'B':
                            matrix2[i][j - 1] = 'B'
                        elif matrixb[i - 1][j-1] == 'B':
                            matrix2[i - 1][j-1] = 'B'
                    elif j == 1:
                        if matrixb[i + 1][j + 1] == 'B':
                            matrix2[i + 1][j + 1] = 'B'
                        elif matrixb[i][j + 1] == 'B':
                            matrix2[i][j + 1] = 'B'
                        elif matrixb[i + 1][j] == 'B':
                            matrix2[i + 1][j] = 'B'
                        elif matrixb[i - 1][j] == 'B':
                            matrix2[i - 1][j] = 'B'
                        elif matrixb[i - 1][j+1] == 'B':
                            matrix2[i - 1][j+1] = 'B'
                    elif j == 8:
                        if matrixb[i - 1][j - 1] == 'B':
                            matrix2[i - 1][j - 1] = 'B'
                        elif matrixb[i][j - 1] == 'B':
                            matrix2[i][j - 1] = 'B'
                        elif matrixb[i - 1][j] == 'B':
                            matrix2[i - 1][j] = 'B'
                        elif matrixb[i + 1][j - 1] == 'B':
                            matrix2[i + 1][j - 1] = 'B'
                        elif matrixb[i + 1][j] == 'B':
                            matrix2[i + 1][j] = 'B'
                    else:
                        if matrixb[i + 1][j + 1] == 'B':
                            matrix2[i + 1][j + 1] = 'B'
                        elif matrixb[i][j + 1] == 'B':
                            matrix2[i][j + 1] = 'B'
                        elif matrixb[i + 1][j] == 'B':
                            matrix2[i + 1][j] = 'B'
                        elif matrixb[i + 1][j - 1] == 'B':
                            matrix2[i + 1][j - 1] = 'B'
                        elif matrixb[i][j - 1] == 'B':
                            matrix2[i][j - 1] = 'B'
                        elif matrixb[i + 1][j-1] == 'B':
                            matrix2[i + 1][j-1] = 'B'
                        if matrixb[i - 1][j + 1] == 'B':
                            matrix2[i - 1][j + 1] = 'B'
                        elif matrixb[i][j + 1] == 'B':
                            matrix2[i][j + 1] = 'B'
                        elif matrixb[i - 1][j] == 'B':
                            matrix2[i - 1][j] = 'B'
                        elif matrixb[i - 1][j - 1] == 'B':
                            matrix2[i - 1][j - 1] = 'B'
                        elif matrixb[i][j - 1] == 'B':
                            matrix2[i][j - 1] = 'B'
                        elif matrixb[i - 1][j-1] == 'B':
                            matrix2[i - 1][j-1] = 'B'

        return matrixb

