from cmath import sqrt
import csv
import math
from pprint import pprint

with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

n = len(data)

def mean(data,n=n):
    total = 0
    for i in data:
        total+=float(i)
    mean = total/n
    return mean

sq_list = []
for x in data:
    a = float(x)-mean(data)
    b = a**2
    sq_list.append(b)
sum = 0
for y in sq_list:
    sum+=float(y)

divided = sum/(n-1)
std_deviation = sqrt(divided)

print(std_deviation)