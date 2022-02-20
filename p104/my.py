import csv
from operator import mod
from statistics import mean, mode
with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

new_data = []
for i in range(len(data)):
    num = data[i][2]
    new_data.append(num)
length = len(new_data)
#mean
sum = 0
for x in new_data:
    sum+=float(x)
mean = sum/length
print('Mean: '+str(mean))
#median
new_data.sort()
if(length%2 == 1):
    c1 = new_data[length/2]
    c2 = new_data[length/2-1]
    median = (c1+c2)/2
else:
    median = new_data[length//2]
print('Median: '+str(median))
#mode
from collections import Counter
data_for_mode = Counter(new_data)
sets = {
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0,
}
for weight, occurence in data_for_mode.items():
    if 75<float(weight)<=85:
        sets['75-85']+=occurence
    elif 85<float(weight)<=95:
        sets['85-95']+=occurence
    elif 95<float(weight)<=105:
        sets['95-105']+=occurence
    elif 105<float(weight)<=115:
        sets['105-115']+=occurence
    elif 115<float(weight)<=125:
        sets['115-125']+=occurence
    elif 125<float(weight)<=135:
        sets['125-135']+=occurence
    elif 135<float(weight)<=145:
        sets['135-145']+=occurence
    elif 145<float(weight)<=155:
        sets['145-155']+=occurence
    elif 155<float(weight)<=165:
        sets['155-165']+=occurence
    elif 165<float(weight)<=175:
        sets['165-175']+=occurence
mode_range,mode_occurence = 0,0
for mode_range,mode_occurence in sets.items():
    if occurence>mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((int(mode_range[0] + mode_range[1])) / 2)
print('Mode: ' + str(mode))