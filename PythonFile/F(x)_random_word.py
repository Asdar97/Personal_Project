import random
import pandas as pd

data = pd.read_csv('random_word.txt')
print(data)


ran = data.RandomWord
rand = random.choice(ran)


def f_predict():
    while True:
        a = input("plz guess an alphabet")
        b = rand
        b = list(b)
        print(b)
        len_b = len(b)
        c = []
        for i in b:
            if a != i:
                d = i.replace(i,"_")
                c.append(d)
            if a == i:
                d = i.replace('a','i')
                c.append(d)
        print(c)
        '''
        f=[]
        alpha = input("put another alphabet")
        for i in b:
            if i != alpha:
                g = i.replace(i,'_')
                f.append(g)
            if i == alpha:
                g = i.replace('alpha','i')
                f.append(g)
        print(f)
        '''
        return c,len_b

def f_combine():
    k, len_b = f_predict()

print(f_combine())







