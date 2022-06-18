# imports
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import plotly.express as px

# data
open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2020, month=10, day=10),
         datetime(year=2020, month=10, day=11),
         datetime(year=2020, month=10, day=12),
         datetime(year=2020, month=10, day=13),
         datetime(year=2020, month=10, day=14)]

# data organized in a pandas dataframe
df=pd.DataFrame(dict(open=open_data,
                    high=high_data,
                    low=low_data,
                    close=close_data,
                    dates=dates))

# transform the data from wide to long
df = pd.melt(df, id_vars=['dates'], value_vars=df.columns[:-1],
         var_name='category', value_name='price')

# setup for a perfect plotly time series figure
fig = px.line(df, x="dates", y="price", title='Prices', color = 'category')

# edit text and hovertemplate
for ser in fig['data']:
    ser['text']=list(set([d.strftime('%Y-%m-%d') for d in df['dates']]))
    ser['hovertemplate']='category=open<br>dates=%{text}<br>price=%{y}<extra></extra>'

fig.show()