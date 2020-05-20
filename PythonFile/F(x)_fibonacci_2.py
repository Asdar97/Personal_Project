#fibonacci
#func import
#func fibonacci
#func list
#func print

import random
import numpy as np
'''
def f_import(import):
    return int(input(import))
'''
def f_calculate(num):
    if num == 0:
        fib = []
    if num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib =[1,1]
        i=1
        while i < (num-1):
            fib.append(fib[i]+fib[i-1])
            i+=1
    print(fib)
'''
def f_print(num):
    fib = f_calculate(num)
    print(fib)
'''
f_calculate(8)

