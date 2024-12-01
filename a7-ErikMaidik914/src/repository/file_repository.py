from src.repository.expense_repo import ExpenseRepository
from src.domain.entities import Expense


class FileRepository(ExpenseRepository):
    def __init__(self, file):
        super(FileRepository, self).__init__()
        self._file_name = file
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self._file_name, "r") as file:
                file_lines = file.readlines()
                list_string_expense = file_lines[len(file_lines) - 1]
                list_string_expense = list_string_expense[:-1]
                list_string_expense = list_string_expense.split(":")
                for expense in list_string_expense:
                    expense = expense.split(";")
                    self._all_expenses[int(expense[0])] = (Expense(int(expense[0]), int(expense[1]), expense[2]))
                file_lines = file_lines[:-1]
                for list_previous_version_expense in file_lines:
                    previous_version = {}
                    list_previous_version_expense = list_previous_version_expense[:-2]
                    list_previous_version_expense = list_previous_version_expense.split(":")
                    for expense in list_previous_version_expense:
                        expense = expense.split(";")
                        # caca
                        previous_version[int(expense[0])] = Expense(int(expense[0]), int(expense[1]), expense[2])
                    self._previous_version.append(previous_version)
                file.close()
        except Exception as e:
            raise e

    def write_to_file(self):
        try:
            with open(self._file_name, "a+") as file:
                file.seek(0)
                data = file.read(100)
                if len(data) > 0:
                    file.write("\n")
                for expense in self.show_all():
                    string_expense = str(expense.get_value()) + ';' + str(
                        expense.get_day()) + ';' + expense.get_type() + ':'
                    file.write(string_expense)
                file.close()

        except Exception as e:
            raise e

    def save(self, expense):
        super(FileRepository, self).save(expense)
        self.write_to_file()

    def remove_last(self):
        try:
            with open(self._file_name, "r+") as file:
                lines_in_file = file.readlines()
                file.seek(0)
                file.truncate()
                lines_in_file[-2] = lines_in_file[-2][:-1]
                file.writelines(lines_in_file[:-1])
            file.close()
        except Exception as e:
            raise e

    def undo(self):
        super(FileRepository, self).undo()
        self.remove_last()
