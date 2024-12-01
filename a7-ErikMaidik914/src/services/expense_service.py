# functiile complexe
import random

from src.domain.entities import Expense
# dam import la entitate
import random


class ExpenseService:
    def __init__(self, expense_repo):
        self.__expense_repo = expense_repo

    def add_expense(self, expense_value, day, type):
        """
        creates and adds a new expense and saves it in the list of expenses with the help of the "save" function present in the expense_repo
        :param expense_value:int>=0
        :param day:int between 1-30
        :param type:string
        :return:
        """
        expense = Expense(expense_value, day, type)
        self.__expense_repo.save(expense)

    def get_all(self):
        """
        #calls the show_all function from repo
        :return:
        """
        return self.__expense_repo.show_all()

    def filter_expense(self, min_value):
        """
        #returns values larger than the given one
        :param min_value: int
        :return: values larger than the given one
        """
        expenses = self.__expense_repo.show_all()

        return [expense for expense in expenses if expense.get_value() >= min_value]

    def undo(self):
        """
        goes one step back in the action list
        :return:
        """
        self.__expense_repo.undo()

    def generate_10(self):
        """
        generates rando items
        :return:
        """
        l = ['house', 'horse', 'nacho', 'apples', 'car', 'pen', 'building']
        if len(self.__expense_repo.show_all()) == 0:
            for _ in range(10):
                self.add_expense(random.randint(1, 1000), random.randint(1, 30), random.choice(l))
