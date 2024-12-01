# list of entities si basic functions -crud create remove update display

class PersonRepo:
    def __init__(self):
        self.__all_persons = {}
        self.__all_activities = {}

    def show_all_pers(self):
        return list(self.__all_persons.values())

    def save_person(self, person):
        self.__all_persons[person.get_person_id()] = person

    def show_all_activities(self):
        return list(self.__all_activities.values())

    def save_activity(self, activity):
        self.__all_activities[activity.get_activity_id()] = activity

    def remove_act(self, activity_id):
        del self.__all_activities[activity_id]

    def remove_pers(self, person_id):
        del self.__all_persons[person_id]

    def add_person_id(self, pers_id, activity):
        for i in self.show_all_activities():
            if i.is_equal(activity):
                i.set_pers_id(pers_id)

    def activity_check(self, person_id):
        for i in self.__all_activities:
            if person_id in i.get_pers_id():
                return False
        return True










