# complex functions
from src.domain.entities import Person
from src.domain.entities import Activity


class Pers_service:
    def __init__(self, repository):
        self.__pers_repo = repository

    def show_pers(self):
        """
        #calls the show_all_pers function from the repo
        :return: all_persons dictionary
        """
        return self.__pers_repo.show_all_pers()

    def show_activity(self):
        """
        #calls the show_all_activities function from the repo
        :return: all_activities dictionary
        """
        return self.__pers_repo.show_all_activities()


    def add_person(self, person_id, name, phone_number):
        """
        #creates a person and adds it to the list with the save_peron function
        :param person_id: int
        :param name: str
        :param phone_number:int
        :return: the newly created person
        """
        person = Person(person_id, name, phone_number)
        self.__pers_repo.save_person(person)

    def add_activity(self, activity_id,persons_id, date, time, description):
        """
        #creates a person and adds it to the list with the save_activity function
        :param activity_id: int
        :param persons_id: list
        :param date: int
        :param time: int
        :param description: str
        :return: the newly created activity
        """
        activity = Activity(activity_id, time, date, description)
        for person_id in persons_id:
            activity.set_pers_id(person_id)
        self.__pers_repo.save_activity(activity)

    def remove_person(self, id):
        """
        #removes a person by id using the del functionality
        :param id: int
        :return:
        """
        return self.__pers_repo.remove_pers(id)

    def remove_activity(self, id):
        """
        #removes an activity by id using the del functionality
        :param id: 1
        :return:
        """
        return self.__pers_repo.remove_act(id)

    def add_to_id_list(self, pers_id, activity):
        """
        #adds automaticaly the person ids to the id list
        :param pers_id:
        :param activity:
        :return:
        """
        return self.__pers_repo.add_person_id(pers_id,activity)

    def act_check(self, id):
        """
        checks if the person is in another act
        :param id: int
        :return:
        """

        return self.__pers_repo.activity_check(id)



