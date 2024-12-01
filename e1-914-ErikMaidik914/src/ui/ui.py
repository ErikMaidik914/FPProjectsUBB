from prettytable import PrettyTable, ALL
import copy

class Ui:
    def __init__(self, service):
        self.__service = service

    def show_matrix(self):
        table = PrettyTable()
        table.hrules = ALL
        table.header = False
        matrix = self.__service.matrix() #empty
        matrix1 = self.__service.stars(copy.deepcopy(matrix))  #only stars
        matrix2 = self.__service.ship(copy.deepcopy(matrix1))  #ship and stars
        matrixb = self.__service.gen_blingon(copy.deepcopy(matrix2)) #visible enemies
        matrixs = self.__service.check_b(copy.deepcopy(matrix2),copy.deepcopy(matrix2)) #hidden enemies
        for row in matrixs:
            table.add_row(row)
        for i in range (9):
            l=[0,1,2,3,4,5,6,7,8]
            table.rows[0][i] = l[i]
        for i in range (8):
            l=['A','B','C','D','E','F','G','H']
            table.rows[i+1][0] = l[i]
        print(table)

    def menu(self):
        print("""
                    SELECT AND INSTRUCTION
                    
            wrap<coordinate>
            fire<coordinate>
            cheat
            map
                    """)
        n = 0
        wlist=['wrap','fire','x','cheat','map']
        matrix = self.__service.matrix()  # empty
        matrix1 = self.__service.stars(copy.deepcopy(matrix))  # only stars
        matrix2 = self.__service.ship(copy.deepcopy(matrix1))  # ship and stars
        matrixb = self.__service.gen_blingon(copy.deepcopy(matrix2))  # visible enemies
        matrixs = self.__service.check_b(copy.deepcopy(matrix2), copy.deepcopy(matrix2))  # hidden enemies
        while True:
            try:
                n = input('YOUR INSTRUCTION IS:')
                #n = n.strip().split(' ')
                if n not in wlist:
                    raise ValueError('wrong input')
                elif n == 'x':
                    print('closed')
                    break

                elif n == 'map':
                    table = PrettyTable()
                    table.hrules = ALL
                    table.header = False
                    for row in matrixs:
                        table.add_row(row)
                    for i in range(9):
                        l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                        table.rows[0][i] = l[i]
                    for i in range(8):
                        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                        table.rows[i + 1][0] = l[i]
                    print(table)

                elif n == 'cheat':
                    table = PrettyTable()
                    table.hrules = ALL
                    table.header = False
                    for row in matrixb:
                        table.add_row(row)
                    for i in range(9):
                        l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                        table.rows[0][i] = l[i]
                    for i in range(8):
                        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                        table.rows[i + 1][0] = l[i]
                    print(table)
                elif n == 'wrap':
                    i = int(input())
                    j = int(input())
                    if self.__service.wrap(i,j,matrixb) == 'o':
                        print('GAME OVER')
                        break
                    elif self.__service.wrap(i,j,matrixb) == 's':
                        print('error')
                    elif self.__service.wrap(i,j,matrixb) == 'w':
                        print('wrong coordinates')
                elif n == 'fire':
                    i = int(input())
                    j = int(input())
                    if self.__service.fire(i,j,matrixb) == 'm':
                        print('miss')
                    elif self.__service.fire(i,j,matrixb) == 'e':
                        print('miss')




            except Exception as e:
                print(e)

