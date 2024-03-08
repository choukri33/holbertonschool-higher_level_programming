#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    num = 0
    for item in my_list[:x]:
        try:
            print("{}".format(item), end='')
            num += 1
        except IndexError:
            break
    print("")
    return num
