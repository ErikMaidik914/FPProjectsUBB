# a3
import copy

from functs import *


def show_menu():
    print("""                       
    TYPE A NUMBER TO SELECT AN INSTRUCTION!
    PRESS 0 to close the program
    PRESS 1 to Generate a list of n random natural numbers
    PRESS 2 to sort the generated list using strand sort
    PRESS 3 to sort the generated list using selection sort
    PRESS 4 to see the time for THE WORST CASE
    PRESS 5 to see the time for THE BEST CASE
    PRESS 6 to see the time for THE AVERAGE CASE""")
    my_list = []
    while True:
        command = 1
        while True:
            try:
                command = int(input("Choose a command: "))
                break
            except ValueError:
                print("You didn't enter a valid command! Try again!")
            if command < 0 or command > 6:
                print("You didn't enter a valid command! Try again!")

        if command == 1:
            my_list = []
            while True:
                try:
                    n = int(input("Choose a number: "))
                    break
                except ValueError:
                    print("You didn't enter a number! Try again!")
            while n > 0:
                my_list.append(random.randint(1, 100))
                n -= 1
            print(f"The list is {my_list} !")
        elif 1 < command < 4:
            if len(my_list) == 0:
                print("There is no list to be sorted yet! Enter 1 to generate a list!")
            else:
                while True:
                    try:
                        step = int(input("Enter an integer: "))
                        break
                    except ValueError:
                        print("You didn't enter an integer! Try again!")
                if command == 2:
                    selection_sort(my_list, step)
                else:
                    strand_sort(my_list, step)
                print(f"The sorted list is {my_list} !")

        elif 3 < command < 7:
            while True:
                try:
                    length = int(input("Enter the starting length!: "))
                    break
                except ValueError:
                    print("You didn't enter a valid length.")
            selection_duration = []
            strand_duration = []
            if command == 4:
                print("         YOU CHOSE THE WORST CASE SCENARIO: ")
                for i in range(5):
                    my_list = generate_list(length)
                    my_list.sort(reverse=True)
                    list_selection = copy.deepcopy(my_list)
                    list_strand = copy.deepcopy(my_list)
                    selection_duration.append(calc_time_sort(selection_time, list_selection))
                    strand_duration.append(calc_time_sort(strand_time, list_strand))
                    length *= 2
            elif command == 5:
                print("         YOU CHOSE THE BEST CASE SCENARIO: ")
                for i in range(5):
                    #my_list = generate_list(length)
                    my_list=list(range(length))
                    list_selection = copy.deepcopy(my_list)
                    list_strand = copy.deepcopy(my_list)
                    selection_duration.append(calc_time_sort(selection_time, list_selection))
                    strand_duration.append(calc_time_sort(strand_time, list_strand))
                    length *= 2
            else:
                print("         YOU CHOSE THE AVERAGE CASE: ")
                for i in range(5):
                    my_list = generate_list(length)
                    list_selection = copy.deepcopy(my_list)
                    list_strand = copy.deepcopy(my_list)
                    selection_duration.append(calc_time_sort(selection_time, list_selection))
                    strand_duration.append(calc_time_sort(strand_time, list_strand))
                    length *= 2
            print(f"The results for selection sort are: {selection_duration} .")
            print(f"The results for strand sort are: {strand_duration}")
        if command == 0:
            print("You've exit the app! :(")
            break


