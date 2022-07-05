import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from datetime import datetime
import plotly.express as px


df2 = pd.read_excel(r'C://Users//John DeForest//OneDrive - Dartmouth College//oldDesk//PMT_3_41.xlsx', sheet_name='weeklystats')

fig2 = go.Figure(go.Scatter(x=df2.datewkstart, y=df2.TSSperhr, mode='lines', name='wkly TSS/hr', hoverinfo='x+y')) #mode markers
#fig2.update_annotations(row=df2.wklyhrs)
fig2.update_xaxes(title_text='date of wk start')
fig2.update_yaxes(title_text='TSS/hr')

pio.write_html(fig2, file='hellooo_world.html', auto_open=True)





#THIS IS W PREV TEST DATA :)
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#
# fig = go.Figure(go.Scatter(x=df.gdpPercap, y=df.lifeExp, text=df.country, mode='markers', name='2007'))
# fig.update_xaxes(title_text='GDP per Capita', type='log')
# fig.update_yaxes(title_text='Life Expectancy')
# #py.iplot(fig, filename='pandas-multiple-scatter')
# pio.write_html(fig, file='hello_world.html', auto_open=True)