from src.repository.expense_repo import ExpenseRepository
import pickle


class BinaryRepository(ExpenseRepository):
    def __init__(self, file):
        super(BinaryRepository, self).__init__()
        self.__file_name = file
        self.read_file()

    def read_file(self):
        file = open(self.__file_name, "rb")
        try:
            data = pickle.load(file)
            self._all_expenses, self._previous_version = data
        except EOFError:
            self._all_expenses = {}
            self._previous_version = []
        file.close()

    def write_file(self):
        data = [self._all_expenses, self._previous_version]
        file = open(self.__file_name, "wb")
        pickle.dump(data, file)
        file.close()

    def save(self, expense):
        super(BinaryRepository, self).save(expense)
        self.write_file()


    def undo(self):
        super(BinaryRepository, self).undo()
        self.write_file()