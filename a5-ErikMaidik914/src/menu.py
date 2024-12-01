# A5

from functs import *



def print_complex_number_list(complex_number):
    if complex_number[1] < 0:
        print(str(complex_number[0]) + " - " + str((-1) * complex_number[1]) + "i")
    else:
        print(str(complex_number[0]) + " + " + str(complex_number[1]) + "i")





def print_complex_number_dictionary(complex_number):
    print(complex_number.get('string_format_of_z'))


def menu():
    print("""
        Options for the list part!
    Option 1:Input a complex number to the list.
    Option 2:Display the list of numbers.
    Option 3:Display the elements of a longest subarray of numbers having increasing modulus.
    Option 4:Display the length and elements of a longest subarray of numbers having increasing modulus(DYNAMIC).

        Options for the dictionary part!
    Option 5:Input a complex number to the list.
    Option 6:Display the list of numbers.
    Option 7:Display the elements of a longest subarray of numbers having increasing modulus.
    Option 8:Display the length and elements of a longest subarray of numbers having increasing modulus(DYNAMIC).


    Option 0:Exit Program.""")
    n = 0
    list_of_complex_numbers = []
    length_list = 0
    dictionary_complex_numbers = []
    length_dictionary = 0
    while True:
        while True:
            try:
                n = int(input("Select an instruction:"))
                break
            except ValueError:
                print(f"Select a valid option!")
            if n < 0 or n > 6:
                print(f"Select a valid option!")

        if n == 0:
            print(f"THE PROGRAM IS CLOSED.")
            break
        elif n == 1:
            print(f"input the real nr a+bi:")
            add_complex_num_to_list(list_of_complex_numbers)
            length_list += 1
        elif n == 2:
            for i in range(length_list):
                print("Element number", i + 1, end=": ")
                print_complex_number_list(list_of_complex_numbers[i])
        elif n == 3:
            if length_list > 0:
                margins_of_subarray = [0, 0]
                length_of_longest_subarray_with_increasing_modulus = modul_list_naive(list_of_complex_numbers,
                                                                                      margins_of_subarray)
                print("Length of the longest subarray with increasing modulus " + str(
                    length_of_longest_subarray_with_increasing_modulus) + " and the sublist is: ")
                i = margins_of_subarray[0]
                while i <= margins_of_subarray[1]:
                    element = list_of_complex_numbers[i]
                    print_complex_number_list(element)
                    i = i + 1
            else:
                print("Empty list")
        elif n == 4:
            max, list = module_list_dynamic(list_of_complex_numbers)
            print(max, list)
        elif n == 5:
            print("Enter your complex number in z= a + bi form:")
            add_complex_number_to_list_in_dictionary_representation(dictionary_complex_numbers)
            length_dictionary = length_dictionary + 1
        elif n == 6:
            for i in range(length_dictionary):
                print_complex_number_dictionary(dictionary_complex_numbers[i])
        elif n == 7:
            if length_dictionary > 0:
                margins_of_subarray = [0, 0]
                length_of_longest_subarray_with_increasing_modulus = modul_dictionary_naive(
                    dictionary_complex_numbers, margins_of_subarray)
                print("Length of the longest subarray with increasing modulus " + str(
                    length_of_longest_subarray_with_increasing_modulus) + " and the sublist is: ")
                i = margins_of_subarray[0]
                while i <= margins_of_subarray[1]:
                    print_complex_number_dictionary(dictionary_complex_numbers[i])
                    i = i + 1
            else:
                print("Empty list")


menu()