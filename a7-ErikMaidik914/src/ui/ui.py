class Console:
    def __init__(self, expense_service):
        self.__expense_service = expense_service

    def menu(self):
        print("""       🐉SELECT A COMMAND🐅

            a --> add an expense
            l --> list of all expenses
            f --> filter expenses
            u --> undo the last operation
            x --> exit""")
        self.__expense_service.generate_10()
        n = 0
        while True:
            try:
                n = str(input("YOUR COMMAND IS-->"))
                if n != 'a' and n != 'l' and n != 'f' and n != 'u' and n != 'x':
                    raise ValueError("OOPS! INVALID INPUT🐊🐊")
                if n == 'x':
                    print('👽PROGRAM CLOSED.👁')
                    break
                elif n == 'a':
                    expense_value = int(input())
                    day = int(input())
                    type = input()
                    if expense_value < 0 or day not in range(1, 30):
                        raise ValueError("💋ERROR✌")
                    self.__expense_service.add_expense(expense_value, day, type)
                elif n == 'l':
                    print(self.__expense_service.get_all())
                elif n == 'f':
                    print(self.__expense_service.filter_expense(min_value=int(input('Your value for sorting is:'))))
                elif n == 'u':
                    self.__expense_service.undo()
            except Exception as e:
                print(e)
