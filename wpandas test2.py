import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from datetime import datetime
import plotly.express as px

# load df
# df2 = pd.read_excel(r'C://Users//John DeForest//OneDrive - Dartmouth College//oldDesk//PMT_3_41.xlsx', sheet_name='weeklystats')
df2 = pd.read_excel(r'C://Users//John DeForest//Desktop//Ski Projects and Analysis//PMT_3_41_BACKUP.xlsx', sheet_name='weeklystats')

# transform data from wide to long
df2 =pd.melt(df2, id_vars=['datewkstart'], value_vars=df2.columns[3:], var_name='category', value_name='TSSperHOUR')

fig2 = px.line(df2, x="datewkstart", y="TSSperHOUR", title='wkly tss/hr', color='category') # if necessary copy the example and then try

#fig2 = go.Figure(go.Scatter(x=df2.datewkstart, y=df2.TSSperhr, mode='lines', name='wkly TSS/hr')) #mode markers
#fig2.update_annotations(row=df2.wklyhrs)
#fig2.update_xaxes(title_text='date of wk start')
#fig2.update_yaxes(title_text='TSS/hr')
for ser in fig2['data']:
    ser['text'] = list(set([d.strftime('%d-%m-%Y') for d in df2['datewkstart']]))
    ser['hovertemplate'] = 'category=open<br>datewkstart=%{text}<br>TSSperhr=%{y}<extra></extra>'

pio.write_html(fig2, file='hellooo_world.html', auto_open=True)





#THIS IS W PREV TEST DATA :)
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#
# fig = go.Figure(go.Scatter(x=df.gdpPercap, y=df.lifeExp, text=df.country, mode='markers', name='2007'))
# fig.update_xaxes(title_text='GDP per Capita', type='log')
# fig.update_yaxes(title_text='Life Expectancy')
# #py.iplot(fig, filename='pandas-multiple-scatter')
# pio.write_html(fig, file='hello_world.html', auto_open=True)