#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    count = 0
    for i in range(list_length):
        try:
            count = (my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError):
            print("division by 0")
            count = 0
        except (TypeError):
            print("wrong type")
            count = 0
        except (IndexError):
            print("out of range")
            count = 0
        finally:
            new_list.append(count)
    return (new_list)