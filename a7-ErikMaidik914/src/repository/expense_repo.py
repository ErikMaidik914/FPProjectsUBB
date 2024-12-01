# multimea entitatilor(lista) si functii basic
import copy


class ExpenseRepository:

    def __init__(self):
        self._all_expenses = {}
        self._previous_version = []

    def show_all(self):
        """
        This method returns a list of entities
        :return: list
        """
        return list(self._all_expenses.values())

    def save(self, expense):
        """
        saves a new entity in the list of entities
        :param expense:entity
        """
        self._previous_version.append(copy.deepcopy(self._all_expenses))
        self._all_expenses[expense.get_value()] = expense

    def undo(self):
        if len(self._previous_version) == 0:
            raise ValueError("no prev version !")
        else:
            self._all_expenses = self._previous_version.pop(-1)
