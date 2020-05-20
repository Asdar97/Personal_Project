#dependency
import numpy as np
#input

num = int(input("insert a number\n"))
#bahagi = list(range(1,num+1))
a = np.arange(1,num,1)
bahagi = list(a)
divisor = []
for number in bahagi:
    if num % number == 0:
        divisor.append(number)
    
print(divisor)
