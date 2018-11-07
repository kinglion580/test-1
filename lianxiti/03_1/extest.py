#!/usr/bin/env python3

num = input("Enter Number:")
try:
    new_num = int(num)
except ValueError:
    print('Parameter Error')
    exit()
print('INT:{}'.format(new_num))
