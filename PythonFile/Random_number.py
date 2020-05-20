#random
import random

while True:

    a = random.randrange(1,9)
    b = int(input("quess the number from 1 to 9 if u r pro\n"))
    if a == b:
        print("the correct number is",a)
        print("congratulation, ur guess is right")
    if a > b:
        print("the correct number is",a)
        print("sorry noob, u guess too low")
    if a < b:
        print("the correct number is",a)
        print("sorry noob, u guess too high")


    loop = input("cont or not")
    if loop == "no":
        break
