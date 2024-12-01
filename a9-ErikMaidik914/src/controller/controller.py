import random


class Controller:
    def __init__(self, repository):
        self.__repository = repository

    def add_sentence(self, sentence):
        return self.__repository.save(sentence)

    def verification(self, sentence):
        self.__repository.verifiy(sentence)

    def choose_random(self):
        l = []
        for i in self.__repository.find_all():
            l.append(i)
        s = random.choice(l)
        return s

    def show_all(self):
        return self.__repository.find_all
