import unittest
from src.service.service import *


class Testing(unittest.TestCase):
    def tester(self,stars):
        m = [[0 for _ in range(9)] for __ in range(9)]
        mz = m
        k = 0
        m = stars(m)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == '*':
                    k +=1
        self.__assertEqual(k, 10)
        self.__assertEqual(m, mz)


