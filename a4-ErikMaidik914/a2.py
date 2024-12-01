# A2
def generated_list(n):
    import random
    random_list = random.sample(range(0, 100), n)
    return random_list


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


def print_partially_sorted_list_after(step, number_steps, previous_step, partial_list):
    if number_steps > previous_step and number_steps % step == 0:
        print(f"your list after this step is:{partial_list}")


def selection_sort(l, size, step):
    number_steps = 0
    for i in range(size):
        min_i = i
        for j in range(i + 1, size):
            if l[j] < l[min_i]:
                min_i = j
        (l[i], l[min_i]) = (l[min_i], l[i])
        previous_number_steps = number_steps
        number_steps = number_steps + 1
        print_partially_sorted_list_after(step, number_steps, previous_number_steps, l)
    return l


def menu():
    print("""
TYPE A NUMBER TO SELECT AN INSTRUCTION!
PRESS 0 to close the program
PRESS 1 to Generate a list of n random natural numbers
PRESS 2 to sort the generated list using strand sort
PRESS 3 to sort the generated list using selection sort
""")

    random_list = []
    while True:
        while True:
            try:
                n = int(input("YOUR INSTRUCTION:"))
                break
            except ValueError:
                print(f"OOPS!This instruction is not available.Please choose another one. ")
        if n == 1:
            try:
                m = int(input("Type the length of the list:"))
            except ValueError:
                print(f"OOPS!This instruction is not available.Please choose another one. ")
            random_list = generated_list(m)
            print(f"The list of {m} random elements is: {random_list}")
        elif n == 2 and not random_list:
            print(f"The list is empty")
        elif n == 2 and random_list:
            s = int(input("Type the step:"))
            print(f"your sorted list by strand sort is{strand_sort(random_list, s)}")
        elif n == 3 and not random_list:
            print(f"The list is empty")
        elif n == 3 and random_list:
            s = int(input("Type the step:"))
            print(f"your sorted list by selection sort is{selection_sort(random_list, len(random_list), s)}")
        elif n == 0:
            print(f"The program is closed")
            break
        else:
            print(f"OOPS!This instruction is not available.Please choose another one. ")


menu()