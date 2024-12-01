

class Repository:

    def __init__(self):
        self.__all_list = []

    def save(self, sentence):
        if self.verify(sentence):
            self.__all_list.append(sentence)

    def verify(self, sentence):
        c = 0
        k = 0
        for i in self.__all_list:
            k = 0
            for j in i:
                if sentence[k] == j:
                    c = c + 1
            k = k + 1
        if c == k:
            return False
        else:
            return True

    def find_all(self):
        return self.__all_list










