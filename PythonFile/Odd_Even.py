#loop
while  True:
    #input
    number = int(input("plz entera number\n"))
    reminder = number%2
    if reminder ==0:
        print("your number is",number, "even number\n")
    else :
        print("your number is",number, "odd number\n")
    loop = input("cont or not?")
    if loop == "no":
        break
     