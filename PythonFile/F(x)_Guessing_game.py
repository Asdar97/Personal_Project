import random

a = random.randrange(0,100)
print(a)
enter = input("plz select a number in ur mind and tell its criteria respect to the random number whether its too low or too high\n")

#while True:
def f_lower(num):
    b = random.randrange(0,num)
    print(b)
    return b

def f_upper(num):
    b = random.randrange(num,100)
    print(b)
    return b


def f_input(level):
    return str(input(level))
    
def f_predict(y):
    if y == "high":
        x = f_lower(a)
        print(z)
    if y == "low":
        x = f_upper(a)
        z = random.randrange(x,100)
        print(z)
    if y == "correct":
        x = True
    return x

f_predict(enter)


'''
    loop = f_predict()
    if loop == True:
        break
'''