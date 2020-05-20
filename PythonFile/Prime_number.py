# ans -prime
# f1 - print prime or not
# f2 - algorith 
# f3 - input

def f_input(x):
    return int(input(x))

def f_differ(number):
    if number == 1:
        prime = False
    if number == 2:
        prime = True
    else:
        prime = True
        z = int(number/2)
        for i in range(2,z+1):
            if number % i == 0:
                prime = False
                break
    return prime

def f_print(y):
    perdana = f_differ(y)
    if perdana:
        tulis = " "
    else:
        tulis = "not"
    print(y,"is",tulis,"prime\n")

while 1 == 1:
    f_print(f_input("enter any number\n"))


#print(f_input("you num"))