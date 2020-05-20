import random

#a = list(random.randrange(1.30))
#b = list(random.randrange(4,25))
a = random.randrange(100,1000)
num1 = []
num2 = []
for x in range(0,a):
    num = random.randrange(1,30)
    nom = random.randrange(4,25)
    num1.append(num)
    num2.append(nom)

    
c = []
for i in num1:
    for j in num2:
        if i == j:
            c.append(i)
#remove same number
c = list(dict.fromkeys(c))


print(c)