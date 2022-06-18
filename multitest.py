# import chart_studio.plotly as py
import plotly.graph_objects as grphobj
from plotly.subplots import make_subplots
# import pandas as pd
# from datetime import datetime, date
import plotly.io as pio
import plotly.express as px
from wklydfcleaner2 import dfretrnclen

# set source excel file and sheet to pull from, run retriever and cleaner to prepare the df
sourceexcelfile = r'C://Users//John DeForest//Desktop//Ski Projects and Analysis//PMT_3_41_BACKUP.xlsx'
sourceexcelsheet = 'weeklystats'
mydf = dfretrnclen(sourceexcelfile, sourceexcelsheet)
#print(mydf.head())

fig2 = make_subplots(specs=[[{"secondary_y": True}]])

print("creating line figure...")

#NEED TO CHANGE CANT USE PX FOR SECOND Y AXIS
#fig2 = px.line(mydf, x="datewkstart", y="TSSperHOUR", title='TSS/hour by Week: A Proxy for Weekly Intensity/Volume Ratio', color='category', markers=True)
#fig2.update_yaxes(range=(0, 75), constrain='domain')

#now add ea of the traces, color goes blue, red, green

fig2.add_trace(grphobj.Scatter(x=mydf["datewkstart"], y=mydf["wklyhrs"], name="totalhours"), secondary_y=False)
fig2.add_trace(grphobj.Scatter(x=mydf["datewkstart"], y=mydf["TSSperHOUR"], name="TSS/hour", fillcolor='#ff0000'), secondary_y=False)
fig2.add_trace(grphobj.Scatter(x=mydf["datewkstart"], y=mydf["wklyTSStot"], name="totalTSS"), secondary_y=True)

fig2.update_traces(marker_line=dict(color='#ff0000'), mode="lines+markers", selector=dict(type='scatter'))
# add titles:
fig2.update_layout(title_text="wklystats")
fig2.update_xaxes(title_text="date (of start of week")


# add multiple y axes titles
fig2.update_yaxes(title_text="<b>TSS/hour and TotalHours", secondary_y=False, range=(0,75), constrain='domain')
fig2.update_yaxes(title_text="<b>total TSS", secondary_y=True)

print("minting data callout labels...")
# print(fig2)
print(fig2['data'][1]['name'])
# order of series: totalhours, TSS/hour, totalTSS

# for ser in fig2['data']:
#     print(ser['name'])
#     ser['text'] = mydf['wklyhrs']
#     # fig2.select_annotations()
#     # fig2.get_subplot()
#     # fig2['data']._get_subplot_rows_columns()[1]
#     # fig2.select_yaxes()
#     print(ser['y'])
# print(fig2)
#
#     if ser['name'] == "totalTSS":
#         ser['hovertemplate'] = 'totTSS: %{y} <br> hours trained: %{text} <br> date(start of week): %{x}<extra></extra>'
#     elif ser['name'] == "TSS/hour":
#         ser['hovertemplate'] = 'TSS/hour: %{y} <br> hours trained: %{text} <br> date(start of week): %{x}<extra></extra>'
#     elif ser['name'] == "totalhours":
#         ser['hovertemplate'] = 'totalhours: %{y} <br> TSS/hr: %<br> date(start of week): %{x}<extra></extra>'
#
# print("writing to display page...")
# pio.write_html(fig2, file='wklyfullmultiy.html', auto_open=True)
# print("done! (plz work oh god)")
