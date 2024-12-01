def modul_dictionary_naive(dictionary_of_complex_numbers, margins):
    list_length = len(dictionary_of_complex_numbers)
    if list_length == 0:
        return 0

    first_element_subarray = 0
    last_element_subarray = 0
    length_subarray = 1
    max_first_element = 0
    max_last_element = 0
    max_length_subarray = 1

    element_of_list_of_complex_numbers = dictionary_of_complex_numbers[0]
    old_element = complex(element_of_list_of_complex_numbers.get('x'), element_of_list_of_complex_numbers.get('y'))
    current_sublist_element = 1
    while current_sublist_element < list_length:
        element_of_list_of_complex_numbers = dictionary_of_complex_numbers[current_sublist_element]
        current_element_of_list = complex(element_of_list_of_complex_numbers.get('x'),
                                          element_of_list_of_complex_numbers.get('y'))
        last_element_subarray = current_sublist_element

        if abs(old_element) > abs(current_element_of_list):
            first_element_subarray = current_sublist_element
            length_subarray = 1
        else:
            length_subarray = length_subarray + 1
            if length_subarray >= max_length_subarray:
                max_length_subarray = length_subarray
                max_first_element = first_element_subarray
                max_last_element = last_element_subarray
        old_element = current_element_of_list
        current_sublist_element = current_sublist_element + 1

    margins[0] = max_first_element
    margins[1] = max_last_element

    return max_length_subarray


def modul_list_naive(list_of_complex_numbers, margins_of_the_subarray):
    length_of_the_list_of_complex_numbers = len(list_of_complex_numbers)
    if length_of_the_list_of_complex_numbers == 0:
        return 0

    first_element_subarray = 0
    last_element_subarray = 0
    length_subarray = 1
    max_first_element = 0
    max_last_element = 0
    max_length_subarray = 1

    element_of_list_of_complex_numbers = list_of_complex_numbers[0]
    old_element = complex(element_of_list_of_complex_numbers[0], element_of_list_of_complex_numbers[1])
    current_sublist_element = 1
    while current_sublist_element < length_of_the_list_of_complex_numbers:

        element_of_list_of_complex_numbers = list_of_complex_numbers[current_sublist_element]
        current_element_of_list = complex(element_of_list_of_complex_numbers[0], element_of_list_of_complex_numbers[1])
        last_element_subarray = current_sublist_element

        if abs(old_element) > abs(current_element_of_list):
            first_element_subarray = current_sublist_element
            length_subarray = 1
        else:
            length_subarray = length_subarray + 1
            if length_subarray >= max_length_subarray:
                max_length_subarray = length_subarray
                max_first_element = first_element_subarray
                max_last_element = last_element_subarray
        old_element = current_element_of_list
        current_sublist_element = current_sublist_element + 1

    margins_of_the_subarray[0] = max_first_element
    margins_of_the_subarray[1] = max_last_element
    return max_length_subarray


def add_complex_num_to_list(complex_list):
    r = int(input("Enter the real part a of the complex number:"))
    i = int(input("Enter the imaginary part of the complex number:"))
    complex_nr = []
    complex_nr.append(r)
    complex_nr.append(i)
    complex_list.append(complex_nr)


def add_complex_number_to_list_in_dictionary_representation(list_of_complex_numbers):
    complex_number_to_add = input()
    sign_real_part = 1

    if complex_number_to_add[0] == "-":
        sign_real_part = -1
        complex_number_to_add = complex_number_to_add[1:]
    index_of_plus_if_it_appears_in_string_of_complex_number = complex_number_to_add.find("+")

    if index_of_plus_if_it_appears_in_string_of_complex_number > -1:
        sign_imaginary_part = 1
        real_part = complex_number_to_add[0:index_of_plus_if_it_appears_in_string_of_complex_number]
        complex_number_to_add = complex_number_to_add[index_of_plus_if_it_appears_in_string_of_complex_number + 1:]
    else:
        index_of_minus_in_string_of_complex_number = complex_number_to_add.find("-")
        sign_imaginary_part = -1
        real_part = complex_number_to_add[0:index_of_minus_in_string_of_complex_number]
        complex_number_to_add = complex_number_to_add[index_of_minus_in_string_of_complex_number + 1:]

    length_of_imaginary_part = complex_number_to_add.find("i")
    imaginary_part = complex_number_to_add[0:length_of_imaginary_part]

    complex_numbers_dictionary = {'x': sign_real_part * float(real_part),
                                  'y': sign_imaginary_part * float(imaginary_part)}

    if sign_imaginary_part == 1:
        complex_numbers_dictionary['string_format_of_z'] = str(complex_numbers_dictionary.get('x')) + "+" + str(
            complex_numbers_dictionary.get('y')) + "i"
    else:
        complex_numbers_dictionary['string_format_of_z'] = str(complex_numbers_dictionary.get('x')) + str(
            complex_numbers_dictionary.get('y')) + "i"
    list_of_complex_numbers.append(complex_numbers_dictionary)


def module_list_dynamic(list):
    max = -1
    firstPosition = 0
    lastPosition = 0
    dp = [[0 for _ in range(len(list))] for _ in range(len(list))]
    for i in range(len(list)):
        for j in range(i + 1):
            if j == i:
                dp[i][j] = 1
            if list[i][0] ^ 2 + list[i][1] ^ 2 > list[i - 1][0] ^ 2 + list[i - 1][1] ^ 2:
                dp[i][j] = dp[i - 1][j] + 1
            if dp[i][j] > max:
                max = dp[i][j]
                firstPosition = i
                lastPosition = j
            else:
                dp[i][j] = 1
    return max + 1, list[firstPosition:lastPosition + 1]





















































"""def modul_list_naive(list_of_complex_numbers, margins_of_the_subarray):
    length_of_the_list_of_complex_numbers = len(list_of_complex_numbers)
    if length_of_the_list_of_complex_numbers == 0:
        return 0
    first_element_subarray = 0
    last_element_subarray = 0
    length_subarray = 1
    max_first_element = 0
    max_last_element = 0
    max_length_subarray = 1

    element_of_list_of_complex_numbers = list_of_complex_numbers[0]
    old_element = complex(element_of_list_of_complex_numbers[0], element_of_list_of_complex_numbers[1])
    current_sublist_element = 1
    while current_sublist_element < length_of_the_list_of_complex_numbers:

        element_of_list_of_complex_numbers = list_of_complex_numbers[current_sublist_element]
        current_element_of_list = complex(element_of_list_of_complex_numbers[0], element_of_list_of_complex_numbers[1])
        last_element_subarray = current_sublist_element

        if abs(old_element) > abs(current_element_of_list):
            first_element_subarray = current_sublist_element
            length_subarray = 1
        else:
            length_subarray = length_subarray + 1
            if length_subarray >= max_length_subarray:
                max_length_subarray = length_subarray
                max_first_element = first_element_subarray
                max_last_element = last_element_subarray
        old_element = current_element_of_list
        current_sublist_element = current_sublist_element + 1

    margins_of_the_subarray[0] = max_first_element
    margins_of_the_subarray[1] = max_last_element
    return max_length_subarray"""



