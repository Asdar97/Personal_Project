import random
import numpy as np

# ------

# ------

def f_random(num=4):
        number = []
        for i in range(0,num):
            x = random.randrange(1,9)
            number.append(x)
        return number
number = f_random()

while True:
    def f_guess():
        print("For every digit that u guessed correctly in the correct place, u have a cow.")
        print("For every digit the u guessed correctly in the wrong place is a bull.")
        guess = (input("plz quess 4 number that randomly generated correctly in sequence\n"))
        guess = [int(i) for i in guess]
        i=0
        cow = 0
        for x in number:
            if guess[i] == number[i]:
                cow+=1
            i+=1

        bull = 0
        for a in guess:
            if a in number:
                bull+=1
        bull=bull-cow
        return number,cow,bull
    def f_correct():
        correct = False
        data = f_guess()
        print(data[0])
        if data[1] == 4:
            print(data[1],"cows and",data[2],"bull, congrats u have guess correctly")
            correct = True
            
        else:
            print(data[1],"cows and",data[2],"bull")
        return correct
    """
    # -- break looping
    f_correct()
    ans = f_guess()
    cow = ans[1]

    #break if correct
    if cow == 4:
        break

    """
    a = f_correct()
    if a is True:
        break


