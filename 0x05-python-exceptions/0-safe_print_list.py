#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    for element in my_list:
        try:
            if count < x:
                print(f"{element}", end='')
                count += 1
        except IndexError:
            break
    print()
    return count
