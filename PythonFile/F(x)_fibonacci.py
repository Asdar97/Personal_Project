#fibonacci

def f_fibonacci():
    num = int(input("plz enter number of fibonacci u want\n"))
    if num == 0:
        fib = []
    if num == 1:
        fib = [1]
    if num == 2:
        fib [ 1,1]
    if num>2:
        fib = [1,1]
        #i=1
        '''
        while i < (num-1):
            x = fib[i]+fib[i-1]
            fib.append(x)
            i += 1
        '''
        for i in range(1,num-1):
            x = fib[i]+fib[i-1]
            fib.append(x)
    return fib

print(f_fibonacci())