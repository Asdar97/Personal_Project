import random
upper = 8
def f_list():
    number = []
    for i in range(0,upper):
        x = random.randrange(1,20)
        number.append(x)
    print(number)
    return number

def f_arrange():
    number = f_list()
    number= [number[0],number[-1]]
    return number

def f_print():
    number = f_arrange()
    print(number)


f_print()