#string 

def f_string():
    string = input("plz write as many word as u want\n")
    string = string.split()
    string = string[::-1]
    
    string = ' '.join(string)
    print(string)
   
    
    

f_string()