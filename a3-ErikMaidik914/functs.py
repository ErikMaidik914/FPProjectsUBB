import time
import random

def generate_list(length):
    generated_list = []
    for i in range(length):
        generated_list.append(random.randint(1, 1000))
    return generated_list


def selection_sort(l, step):
    number_steps = 0
    for i in range(len(l)):
        min_i = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_i]:
                min_i = j
        (l[i], l[min_i]) = (l[min_i], l[i])
        previous_number_steps = number_steps
        number_steps = number_steps + 1
        print_partially_sorted_list_after(step, number_steps, previous_number_steps, l)
    return l



def print_partially_sorted_list_after(step, number_steps, previous_step, partial_list):
    if number_steps > previous_step and number_steps % step == 0:
        print(f"your list after this step is:{partial_list}")


def strand_sort(random_list, step):
    number_steps = 0
    if len(random_list) < 2:
        return random_list
    output = []
    while random_list:
        i = 0
        sublist = []
        sublist.append(random_list.pop())
        while i < len(random_list):
            num = random_list[i]
            if num > sublist[-1]:
                sublist.append(num)
                del random_list[i]
            else:
                i = i + 1
        output = merge(list(output), sublist)
        previous_number_steps = number_steps
        number_steps = number_steps + 1
        print_partially_sorted_list_after(step, number_steps, previous_number_steps, output)
    return output


def merge(list_1, list_2):
    i = 0
    j = 0
    merged_list = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] > list_2[j]:
            merged_list.append(list_2[j])
            j = j + 1
        else:
            merged_list.append(list_1[i])
            i = i + 1
    merged_list = merged_list + list_1[i:]
    merged_list = merged_list + list_2[j:]
    return merged_list


def strand_time(random_list):
    if len(random_list) < 2:
        return random_list
    output = []
    while random_list:
        i = 0
        sublist = []
        sublist.append(random_list.pop(0))
        while i < len(random_list):
            num = random_list[i]
            if num > sublist[-1]:
                sublist.append(num)
                del random_list[i]
            else:
                i = i + 1
        output = merge(list(output), sublist)
    return output

def selection_time(l):
    for i in range(len(l)):
        min_i = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_i]:
                min_i = j
        (l[i], l[min_i]) = (l[min_i], l[i])
    return l



def calc_time_sort(function,list):
    start = time.time()
    function(list)
    stop = time.time()
    return round((stop - start)*1000, 5)
