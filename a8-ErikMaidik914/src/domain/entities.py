# setters+getters si entitatile

class Person:
    def __init__(self, person_id, name, phone_number):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    def get_person_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def set_person_id(self, new_person_id):
        self.__person_id = new_person_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def __repr__(self):
        return f"{self.__person_id} - {self.__name} - {self.__phone_number}"


class Activity:
    def __init__(self, activity_id, date, time, description):
        self.__activity_id = activity_id
        self.__pers_id = []
        self.__date = date
        self.__time = time
        self.__description = description

    def get_activity_id(self):
        return self.__activity_id

    def get_pers_id(self):
        return list(self.__pers_id)

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def set_activity_id(self, new_activity_id):
        self.__activity_id = new_activity_id

    def set_pers_id(self, new_pers_id):
        self.__pers_id.append(new_pers_id)

    def set_date(self, new_date):
        self.__date = new_date

    def set_time(self, new_time):
        self.__time = new_time

    def set_description(self, new_description):
        self.__description = new_description

    def __repr__(self):
        return f"{self.__activity_id} - {self.__pers_id} - {self.__date} - {self.__time} - {self.__description} "

    def is_equal(self, activity):
        if self.__activity_id == activity.get_activity_id(activity):
            return True
        else:
            return False

