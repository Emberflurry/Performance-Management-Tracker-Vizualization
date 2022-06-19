# import chart_studio.plotly as py
import plotly.graph_objects as grphobj
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.express as px
from wklydfcleaner2 import dfretrnclen
import pandas as pd
from datetime import datetime, date

# set source excel file and sheet to pull from, run retriever and cleaner to prepare the df
sourceexcelfile = r'C://Users//John DeForest//Desktop//Ski Projects and Analysis//PMT_3_41_BACKUP.xlsx'
sourceexcelsheet = 'dailystats'  # try to pull ALREADY CALCD BY EXCEL PMT VALS first (in future redo formulas?)

# READ EXCEL INTO PANDAS DF:
print("getting date...")
today = date.today().strftime("%m/%d/%Y").split('/')
tyear = int(today[2])
tmonth = int(today[0])
tday = int(today[1])
# print(tyear,"/",tmonth,"/",tday)
# print(tyear)

# load df
print("loading dataframe...")
mydf = pd.read_excel(sourceexcelfile, sheet_name=sourceexcelsheet)

# round the values (NOT the dates)
# TODO CHANGE THIS TO MATCH ACTUAL DATA HEADERS IN TRAININGDATA SHEET
print("cleaning values...")
mydf.wklyhrs = mydf.wklyhrs.round(1) #TODO
mydf.wklyTSStot = mydf.wklyTSStot.round(1)  #TODO
mydf.TSSperhr = mydf.TSSperhr.round(1)  #TODO

# get rid of empty entries n stuff earlier (farther back in time than log entries)
print("emptying the trash...")
for i, r in mydf.iterrows():
    if r['wklyhrs'] > 0 or r['wklyTSStot'] > 0 or r['TSSperhr'] > 0:
        # print(df2.iloc[i])
        break
    elif r['wklyhrs'] <= 0 or r['wklyTSStot'] <= 0 or r['TSSperhr'] <= 0:
        mydf.drop(index=i, inplace=True)

# get rid of all weekly entries yet to come
for i, r in mydf.iterrows():
    vals = str(r['datewkstart'])[0:10].split('-')
    day = int(vals[2])
    month = int(vals[1])
    year = int(vals[0])
# print(year, month, day)

    if datetime(year, month, day) > datetime(tyear, tmonth, tday):
        mydf.drop(index=i, inplace=True)

# print(df2.head())
# print(df2.tail())
# check df for correct start and end points + values

# convert and display
print("melting dataframe...")
mydf = pd.melt(mydf, id_vars=['datewkstart', 'wklyhrs', 'wklyTSStot'], value_vars=mydf.columns[3:], var_name='category', value_name='TSSperHOUR')
# print(df2.head())

# ^ READING AND CLEANING INTO PD DF
# _________________________________________________________________________________________
# v CREATION OF FIGURES N PLOTS

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

for ser in fig2['data']:
    print(ser['name'])
    ser['text'] = mydf['wklyhrs']
    # fig2.select_annotations()
    # fig2.get_subplot()
    # fig2['data']._get_subplot_rows_columns()[1]
    # fig2.select_yaxes()
    # print(ser['y'])
# print(fig2)

    if ser['name'] == "totalTSS":
        ser['hovertemplate'] = 'totTSS: %{y} <br> hours trained: %{text} <br> date(start of week): %{x}<extra></extra>'
    elif ser['name'] == "TSS/hour":
        ser['hovertemplate'] = 'TSS/hour: %{y} <br> hours trained: %{text} <br> date(start of week): %{x}<extra></extra>'
    elif ser['name'] == "totalhours":
        ser['hovertemplate'] = 'totalhours: %{y} <br> TSS/hr: %<br> date(start of week): %{x}<extra></extra>'
#
# print("writing to display page...")
pio.write_html(fig2, file='wklyfullmultiy.html', auto_open=True)
# print("done! (plz work oh god)")
