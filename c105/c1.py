import csv
import pandas as pd
import plotly.express as px

with open('class1.csv',newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

total_marks = 0
legnth = len(data)
for i in data:
    total_marks+=int(i[1])
mean = total_marks/legnth
print('Mean: '+str(mean))

df = pd.read_csv('class1.csv')
fig = px.scatter(df,x='Student Number', y = 'Marks')
fig.update_layout(shapes = [
    dict(
        type='line',
        y0 = mean,
        y1 = mean,
        x0 = 0,
        x1 = legnth
    )
])
fig.update_yaxes(rangemode='tozero')
fig.show()