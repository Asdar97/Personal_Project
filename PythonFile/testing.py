a = [1,2,3,4]
b = [1,3,2,4]
i=0
for x in a:
    print(a[i])
    print(b[i])
    if a[i] == b[i]:
        print("true")
    else:
        print("false")
    i+=1
