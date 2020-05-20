#find overlapping in 2 different file
import pandas as pd

prime = pd.read_csv('prime_number.txt')
happy = pd.read_csv('happy_number.txt')
#print(prime.prime_number)
def f_overlapping():
    overlap = 0
    for x in prime.prime_number:
        for y in happy.happy_number:
            if x == y:
                overlap+=1
                print(x,y)
    return overlap

print("total number that overlapping are",f_overlapping())
