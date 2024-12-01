#entitatile + getters and setters
class Expense:

    def __init__(self, expense_value, day, type):
        # Constructor
        self.__expense_value = expense_value
        self.__day = day
        self.__type = type

    def get_day(self):
        return self.__day

    def set_day(self, new_day):
        self.__day = new_day

    def get_value(self):
        return self.__expense_value

    def set_value(self, new_value):
        self.__expense_value = new_value

    def get_type(self):
        return self.__type

    def set_type(self, new_type):
        self.__type = new_type

    def __repr__(self):
        return f"{self.__expense_value}- {self.__day} - {self.__type}"