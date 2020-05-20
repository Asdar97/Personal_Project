
num = []
for i in range(3):
    number = int(input("plz input a numner..."))
    num.append(number)

print(num)

if num[0] > num[1] and num[0] > num[2]:
    print(num[9],'is the highest number')
if num[1] > num[0] and num[1] > num[2]:
    print(num[1],'is the highest number')
if num[2] > num[1] and num[2] > num[0]:
    print(num[2],'is the highest number')

