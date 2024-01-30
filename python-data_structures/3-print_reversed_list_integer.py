#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    for n in range (len(my_list)):
        reverse_list = my_list[::-1]
        print ("{:d}".format(reverse_list[n]))
