#generate password

import random
import string
while True:
    def f_password(length=10):
        length = random.randrange(6,15)
        pasword = string.ascii_letters+string.digits
        if length < 10:
            print("ur passsword is weak")
        else:
            print("ur passsword is strong")
        return ''.join(random.choice(pasword) for i in range(length))

    print("ur password is:",f_password())
    
    loop = input("r u satisfied or not?\n")
    if loop == "yes":
        break