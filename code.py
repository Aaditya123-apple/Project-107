import pandas as pd
import plotly.express as px
import csv

df=pd.read_csv('student.csv')
mean=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()

#df=pd.read_csv('marks.csv')
#mean=df.groupby(['Marks In Percentage','Days Present']).mean()

fig=px.scatter(mean, x='student_id', y='level', size='attempt', color='attempt')
fig.show()
