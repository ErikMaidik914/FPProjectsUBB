import copy
import random


def create_person(fp1, fp2, fp3):
    """We calculate the average and the total sum of the grades p1,p2 and p3 and we intoduce them along with p1,p2,p3 in a dictionary named person"""
    try:
        fp1 = int(fp1)
        fp2 = int(fp2)
        fp3 = int(fp3)
    except ValueError:
        return False
    fscore = fp1 + fp2 + fp3
    faverage = (fp1 + fp2 + fp3) // 3
    person = {'p1': fp1, 'p2': fp2, 'p3': fp3, 'score': fscore, 'average': faverage}
    return person


def add_to_list(person_list, given_person):
    """
    we append the given participant to the list
    :param given_person:
    :param person_list:
    :return:person_list
    """
    person_list.append(given_person)


def get_p1(person):
    return person['p1']


def get_p2(person):
    return person['p2']


def get_p3(person):
    return person['p3']


def get_score(person):
    return person['score']


def get_average(person):
    return person['average']


def generate_people(length):
    """we generate 3 random grades from 0 to 10 using the random function, then by using the create function that we wrote, we form a dictionary for each person and
    we add it to the list"""
    person = []
    while len(person) < length:
        new_person = create_person(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
        person.append(new_person)
    return person



