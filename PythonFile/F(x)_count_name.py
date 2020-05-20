#kira nama
import pandas as pd
'''
#open file
nama =  open('namelist.txt', 'r').read()
nama = []
lea = 0
for i in nama:
    if i == 'Lea':
        lea+=1
print(lea)
'''

nama = pd.read_csv('namelist.txt')
#print(nama.index)
#sprint(nama.NAME[1])
#print(nama)

def f_name(y):
    lea=0
    for x in nama.NAME:
        if x == y:
            lea+=1
    return lea

print("Total name Lea",f_name('Lea'))
print("Total name Darth",f_name('Darth'))
print("Total name Luke",f_name('Luke'))

    