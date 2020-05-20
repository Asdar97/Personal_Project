import random

def f_random():
    data = []
    for i in range(0,5):
        a = random.randrange(1,9)
        data.append(a)
        data.sort()
    return data

def f_number():
    data = []
    a = random.randrange(1,9)
    data.append(a)
    return a

def f_check():
    data = f_random()
    num = f_number()
    print(num,data)
    if num in data:
        equal = ''
    else:
        equal = 'not'
    '''
    for a in data:
        equal = 'not'
        if num[0] == data[i]:
            equal = ''
            i+=1
        #else:
            #equal = 'not'
    '''
    return equal

print("the number is",f_check(),"in the list")