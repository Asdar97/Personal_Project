# looping using while
while True: 
# input
    name = input("your name? \n")
    age = int(input("your age? \n"))
#  calculate
    x = 100 - age
    current = 2014
    ans = str(x + current)
    print(name + ",year you get 100 is "+ ans)
    loop = input("cont or not?")
    if loop == "no":
        break