class Repository:
    def __init__(self):
        self.__matrix = [[0 for _ in range(9)] for __ in range(9)]

    def get_matrix(self):
        return self.__matrix


