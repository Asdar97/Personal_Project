import random
import numpy as np

def f_list():
    x = []
    for i in range(0,10):
        a = random.randrange(1,10)
        x.append(a)
    print(x)
    return x

def f_return():
    c = f_list()
    c = list(dict.fromkeys(c))
    print(c)

f_return()