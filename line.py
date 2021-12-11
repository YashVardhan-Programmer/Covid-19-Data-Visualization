import pandas as pd
import plotly_express as px

df = pd.read_csv('Covid_Data.csv')

fig = px.line(df, x = 'date', y = 'cases', title='Covid Cases', color='country')
fig.show()