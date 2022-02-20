import pandas as pd
import plotly_express as px
#creating an empty data frmae
'''df = pd.DataFrame() 
print(df)'''

'''data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)'''

df = pd.read_csv('csv files/line_chart.csv')

fig = px.line(df, x = 'Year', y ='Per capita income', color ='Country', title = "Per Capita Income")
fig.show()