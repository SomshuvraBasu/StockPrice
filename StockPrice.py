import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020,4,25)
end = dt.datetime(2020,5,10)

df = web.DataReader('^BSESN', 'yahoo', start, end)

ds=df['Adj Close']
#dp=df['']
cs=ds.values.tolist()

#ps=dp.values.tolist()
print(df['Adj Close'])
print(df)
print(cs)
#print(ps)
