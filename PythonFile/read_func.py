#call pandas
import pandas as pd

# readfile
data = pd.read_csv("data.txt")
#data = list(data)
print(data)

def f_darab(data):
    data = data * 2
    data.to_csv("data.txt")
    return data

f_darab(data)