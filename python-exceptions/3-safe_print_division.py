#!/usr/bin/python3
def safe_print_modulo(a, b):
    try:
        div = a % b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(mod))
    return div