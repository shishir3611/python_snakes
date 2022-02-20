import pandas as pd
import plotly_express as px

df = pd.read_csv('csv files/data.csv')

fig = px.bar(df, x = 'Country', y = 'InternetUsers')
fig.show()