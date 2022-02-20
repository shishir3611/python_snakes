from cmath import sqrt
import csv
import math

with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total+=int(i)
    mean = total/n
    return mean

sq_list = []
for x in data:
    a = int(x)-mean(data)
    b = a**2
    sq_list.append(b)
sum = 0
for y in sq_list:
    sum+=int(y)
