#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_of_args = len(sys.argv)
    total_sum = 0

    for i in range(1, num_of_args):
        total_sum += int(sys.argv[i])

    print(total_sum)
