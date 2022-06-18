# import chart_studio.plotly as py
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import plotly.io as pio
# import plotly.express as px
import pandas as pd
from datetime import datetime, date


def dfretrnclen(myfilewpath, mysheetname):
    print("getting date...")
    today = date.today().strftime("%m/%d/%Y").split('/')
    tyear = int(today[2])
    tmonth = int(today[0])
    tday = int(today[1])
# print(tyear,"/",tmonth,"/",tday)
# print(tyear)

# load df
    print("loading dataframe...")
    df2 = pd.read_excel(myfilewpath, sheet_name=mysheetname)

# round the values (NOT the dates)
    print("cleaning values...")
    df2.wklyhrs = df2.wklyhrs.round(1)
    df2.wklyTSStot = df2.wklyTSStot.round(1)
    df2.TSSperhr = df2.TSSperhr.round(1)

# get rid of empty entries n stuff earlier (farther back in time than log entries)
    print("emptying the trash...")
    for i, r in df2.iterrows():
        if r['wklyhrs'] > 0 or r['wklyTSStot'] > 0 or r['TSSperhr'] > 0:
            # print(df2.iloc[i])
            break
        elif r['wklyhrs'] <= 0 or r['wklyTSStot'] <= 0 or r['TSSperhr'] <= 0:
            df2.drop(index=i, inplace=True)

# get rid of all weekly entries yet to come
    for i, r in df2.iterrows():
        vals = str(r['datewkstart'])[0:10].split('-')
        day = int(vals[2])
        month = int(vals[1])
        year = int(vals[0])
    # print(year, month, day)

        if datetime(year, month, day) > datetime(tyear, tmonth, tday):
            df2.drop(index=i, inplace=True)

# print(df2.head())
# print(df2.tail())
# check df for correct start and end points + values

# convert and display
    print("melting dataframe...")
    df2 = pd.melt(df2, id_vars=['datewkstart', 'wklyhrs', 'wklyTSStot'], value_vars=df2.columns[3:], var_name='category', value_name='TSSperHOUR')
# print(df2.head())
    return df2
