class Console:
    def __init__(self, person_service):
        self.__person_service = person_service

    def menu(self):
        print("""       🐉SELECT A COMMAND🐅

                    aa --> add an activity
                    ap --> add a person
                    la --> list of all activities
                    lp --> list of all persons
                    ra --> remove activity
                    rp --> remove person
                    ua --> update activity
                    up -->update person
                    f --> filter 
                    u --> undo the last operation
                    x --> exit""")

        n = 0
        check_list = []
        while True:
            try:
                n = input("Your command is:")
                if n not in ['x', 'aa', 'la', 'ap', 'lp', 'ra', 'rp', 'ua', 'up', 'f', 'u']:
                    raise ValueError("OOPSIE!")
                if n == 'x':
                    print('👽PROGRAM CLOSED.👁')
                    break
                elif n == 'ap':
                    person_id = input()
                    check_list.append(person_id)
                    name = input()
                    phone_number = input()
                    self.__person_service.add_person(person_id, name, phone_number)
                elif n == 'lp':
                    print(self.__person_service.show_pers())
                elif n == 'la':
                    print(self.__person_service.show_activity())
                elif n == 'aa':
                    while True:
                        activity_id = input("activity_id:")
                        persons_id = input("person's id that participates in this activity:").split()
                        try:
                            for i in range(len(persons_id)):
                                if persons_id[i] not in check_list:
                                    raise ValueError
                                else:
                                    if not self.__person_service.act_check(persons_id[i]):
                                        raise ValueError
                            persons_id = [int(pers_id) for pers_id in persons_id]
                        except ValueError:
                            print("Wrong input")
                            break
                        date = input("date:")
                        time = input("time:")
                        description = input("description:")
                        self.__person_service.add_activity(activity_id,persons_id, date, time, description)
                        break
                elif n == 'rp':
                    id = input()
                    self.__person_service.remove_person(id)
                elif n == 'ra':
                    id = input()
                    self.__person_service.remove_activity(id)
                else:
                    print('nacho')
            except Exception as e:
                print(e)
