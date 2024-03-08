def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for item in my_list[:x]:
        if isinstance(item, int):
            print("{:d}".format(item), end='')
            num += 1
    print()
    return num