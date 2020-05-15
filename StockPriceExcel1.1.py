import xlsxwriter
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020,4,25)
end = dt.datetime(2020,5,10)

df = web.DataReader('^BSESN', 'yahoo', start, end)
#print(df.head())

workbook = xlsxwriter.Workbook('StockPrices.xlsx')
ws = workbook.add_worksheet("Sensex")

row = 0
col = 0
j = 0

ds=df['Adj Close']


price=ds.values.tolist()
print(ds)
date=df.index.values.tolist()
print(date)
print(price)

for i in price:
    ws.write(row, col, date[j])
    ws.write(row, col + 1, price[j])
    row+=1
    j+=1

workbook.close()

    
