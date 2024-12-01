from functions import *


def get_command():
    command = input('Enter a command: ')
    command = command.split()
    return command


def add_person(person_list, *scores):
    scores = scores[0]
    if len(scores) != 3:
        print('Invalid command! 🤦‍🤦‍')
        return
    try:
        p1 = int(scores[0])
        p2 = int(scores[1])
        p3 = int(scores[2])
        if p1 < 0 or p1 > 10 or p2 < 0 or p2 > 10 or p3 < 0 or p3 > 10:
            print('invalid input 🐱')
            return
        else:
            new_person = create_person(p1, p2, p3)
            add_to_list(person_list, new_person)
    except ValueError as ve:
        print('Invalid command! 🤦‍🤦‍', ve)


def insert_person(person_list, *scores):
    scores = scores[0]
    if len(scores) != 5:
        print('Invalid command! 🤦‍🤦‍')
        return
    try:
        p1 = int(scores[0])
        p2 = int(scores[1])
        p3 = int(scores[2])
        if p1 < 0 or p1 > 10 or p2 < 0 or p2 > 10 or p3 < 0 or p3 > 10:
            print('invalid input 🐱')
            return
        else:
            new_person = create_person(p1, p2, p3)
        if scores[3].lower() != 'at':
            print('invalid input 🐱')
            return
        position = int(scores[4]) - 1
        if position < 1 or position > len(person_list):
            raise ValueError('😎')
        person_list.insert(position, new_person)
    except ValueError:
        print('Invalid command! 🤦‍🤦‍')


def remove_person(person_list, *args):
    args = args[0]
    if len(args) == 1:
        i = 0
        try:
            p = int(args[0])
            if p < 0 or p > len(person_list):
                print('Invalid command! 🤦‍🤦')
            else:
                for person in person_list:
                    i = i + 1
                    if i == p:
                        person.update({'p1': 0, 'p2': 0, 'p3': 0, 'score': 0, 'average': 0})
        except ValueError:
            print('Invalid input! 🤑😰😱')
    elif len(args) == 3:
        j = 0
        try:
            p = int(args[0])
            l = int(args[2])
            if p < 0 or p > len(person_list) or p > len(person_list) or l < p or l == p or args[1] != 'to':
                print('Invalid command! 🤦‍🤦')
            else:
                for person in person_list:
                    j = j + 1
                    if j == p or (j > p and j < l) or j == l:
                        person.update({'p1': 0, 'p2': 0, 'p3': 0, 'score': 0, 'average': 0})
        except ValueError:
            print('Invalid input! 🤑😰😱')
    elif len(args) == 2:
        try:
            s = args[0]
            p = int(args[1])
            if p > 10 or p < 0 or (s != '=' and s != '>' and s != '<'):
                print('Invalid command! 🤦‍🤦')
            else:
                for person in person_list:
                    if s == '=':
                        if person['average'] == p:
                            person.update({'p1': 0, 'p2': 0, 'p3': 0, 'score': 0, 'average': 0})
                    elif s == '>':
                        if person['average'] > p:
                            person.update({'p1': 0, 'p2': 0, 'p3': 0, 'score': 0, 'average': 0})
                    elif s == '<':
                        if person['average'] < p:
                            person.update({'p1': 0, 'p2': 0, 'p3': 0, 'score': 0, 'average': 0})
        except:
            print('Invalid input! 🤑😰😱')


def remove_score(person_list, *args):
    args = args[0]
    pass


def replace_person(person_list, *args):
    args = args[0]
    i = 0
    try:
        num = int(args[0])
        p = str(args[1])
        s = int(args[3])
        if s > 10 or s < 0 or num > len(person_list) or num < 0 or args[2] != 'with':
            print('Invalid command! 🤦‍🤦')
        else:
            if p == 'p1':
                for person in person_list:
                    if i == num:
                        person.update({'p1': s})
                    i = i + 1
            elif p == 'p2':
                for person in person_list:
                    if i == num:
                        person.update({'p2': s})
                    i = i + 1
            elif p == 'p3':
                for person in person_list:
                    if i == num:
                        person.update({'p3': s})
                    i = i + 1
            else:
                print("ERRORRRRRRRRRRR")
    except:
        print('Invalid command! 🤦‍🤦')


def print_all(person_list, *args):
    args = args[0]
    if len(args) == 0:
        print(person_list)
    elif len(args) == 1:
        if args[0] == 'sorted':
            new_list = copy.deepcopy(person_list)
            new_list.sort(key=get_average)
            new_list.reverse()
            print(new_list)
        else:
            print('Invalid command!')
    elif len(args) == 2:
        sign = args[0]
        new_l = []
        try:
            number = int(args[1])
            if sign == '>':
                for person in person_list:
                    if person['average'] > number:
                        new_l.append(person)
            elif sign == '=':
                for person in person_list:
                    if person['average'] == number:
                        new_l.append(person)
            elif sign == '<':
                for person in person_list:
                    if person['average'] < number:
                        new_l.append(person)
            if len(new_l) == 0:
                print('No results meeting the demand.')
            else:
                for i in new_l:
                    print(i)
        except:
            print('Invalid command')
            return
    else:
        print('Invalid command')


def top(person_list, *args):
    args = args[0]
    if len(args) == 1:
        try:
            v = int(args[0])
            if v > 10 or v < 0:
                print('Invalid command! 🤐')
            c = 0
            new_list = copy.deepcopy(person_list)
            new_list.sort(key=get_average)
            new_list.reverse()
            for i in new_list:
                if c == v:
                    break
                c = c + 1
                print(i)
        except ValueError:
            print('Invalid command! 🤐')
    elif len(args) == 2:
        try:
            p = args[1]
            v = int(args[0])
            if args[1] == 'p1':
                c = 0
                new_list = copy.deepcopy(person_list)
                new_list.sort(key=get_p1)
                new_list.reverse()
                for i in new_list:
                    if c == v:
                        break
                    c = c + 1
                    print(i)
            elif args[1] == 'p2':
                k = 0
                new_l = copy.deepcopy(person_list)
                new_l.sort(key=get_p2)
                new_l.reverse()
                for j in new_l:
                    if k == v:
                        break
                    k = k + 1
                    print(j)
            elif args[1] == 'p3':
                h = 0
                new_lis = copy.deepcopy(person_list)
                new_lis.sort(key=get_p3)
                new_lis.reverse()
                for w in new_lis:
                    if h == v:
                        break
                    h = h + 1
                    print(w)
            else:
                print('Invalid command! 🤐')
        except:
            print('Invalid command! 🤐')


def execute_command(person_list, command, args):
    all_commands = {
        'add': add_person,
        'remove': remove_person,
        'insert': insert_person,
        'list': print_all,
        'top': top,
        'replace': replace_person}
    try:
        all_commands[command](person_list, args)
    except:
        print('Invalid command! 🤦‍🤦')


def show_menu():
    print("""
    WELCOME CHOOSE AN INSTRUCTION!
    1.add <P1 score> <P2 score> <P3 score>
    2.insert <P1 score> <P2 score> <P3 score> at <position>
    -----------------------------------------------------------------
    3.remove <position>
    4.remove <start position> to <end position>
    5.replace <participant position> <P1 | P2 | P3> with <new score>
    -----------------------------------------------------------------
    6.list
    7.list sorted
    8.list [ < | = | > ] <score>
    -----------------------------------------------------------------
    9.top <number>
    10.top <number> <P1 | P2 | P3>
    11.remove [ < | = | > ] <score>
    12.undo
    0.bye - close the program

    """)


def run_console():
    person_list = generate_people(10)
    list_of_undoable_commands = ['add', 'replace', 'remove', 'insert']
    person_list_history = []
    while True:
        show_menu()
        commands = get_command()
        command = commands[0]
        args = []
        try:
            args = commands[1:]
        except:
            pass
        if command == 'bye' or command == 'exit':
            print('You\'ve left the app... 🐱‍🚀✨🌹')
            break
        elif command == 'undo':
            if len(person_list_history) == 0:
                print('There is nothing left to undo! 😝')
            else:
                person_list = person_list_history.pop()
        else:
            person_list_copy = copy.deepcopy(person_list)
            if command in list_of_undoable_commands:
                execute_command(person_list, command, args)
                if person_list_copy != person_list:
                    person_list_history.append(person_list_copy)
            else:
                execute_command(person_list, command, args)
