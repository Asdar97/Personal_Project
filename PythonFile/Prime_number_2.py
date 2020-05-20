#primenumber
import numpy as np
'''
while True:
    prime = int(input("input any number\n"))
    num = np.arange(2,prime-1,1)
    num = list(num)
    c =[]
    d =[]

    for i in num:
        x = prime%i
        c.append(x)
            
    for j in c:
        if j == 0:
            d.append(j)
    #print(d)
    v = len(d)
    if v == 0:
        print('prime')
    else:
        print('not prime')


    loop = input("cont or not")
    if loop == "no":
        break
'''
while True:
    prime = int(input("enter a number\n"))
    #num = np.arange(2,prime-1,1)
    #num = list(num)
    c = []
    d = []

    for i in range(2,prime-1,1):
        x = prime%i
        c.append(x)
        
    for j in c:
        if j == 0:
            d.append(j)
    
    v = len(d)
    if v == 0:
        print("ur number is prime")
    else:
        print("ur number not a prime")