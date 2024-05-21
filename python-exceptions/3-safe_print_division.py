#!/usr/bin/python3
def safe_print_modulo(a, b):
    try:
        mod = a % b
    except (TypeError, ZeroDivisionError):
        mod = None
    finally:
        print("Inside result: {}".format(mod))
    return mod