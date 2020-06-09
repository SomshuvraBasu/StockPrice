import os
import xlsxwriter
import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from tkinter import *
import mysql.connector as m
import tkinter.messagebox as mb
import GUI
import sqlmod

if os.path.exists("StockPrices.xlsx"):
    os.remove("StockPrices.xlsx")
else:
    pass

GUI.loop()

style.use('ggplot')

#s_id = input("Enter Stock ID: ")
#s_name = input("Enter Stock Name: ")


def stock(s_id, s_name):
    
    start = dt.datetime(1985, 1, 1)
    today = date.today()

    df = web.DataReader(s_id, 'yahoo', start, today)
    dm = web.DataReader(s_id, 'yahoo', start, today)

    print(df)

    df['90ma'] = df['Adj Close'].rolling(window=90, min_periods=0).mean()
    df.dropna(inplace=True)

    ds = df[['Adj Close', '90ma']]

    workbook = xlsxwriter.Workbook('StockPrices.xlsx')
    ws = workbook.add_worksheet(s_name)

    row = 0
    col = 0
    j = 0

    dw = dm['Adj Close']
    dq = df['90ma']
    mov_avg = dq.values.tolist()
    price = dw.values.tolist()

    print(price)

    ws.write(row, col + 1, 'AdjClose')
    ws.write(row, col + 2, 'Moving')

    for i in price:
        ws.write(row + 2, col + 1, price[j])
        ws.write(row + 2, col + 2, mov_avg[j])
        row += 1
        j += 1

    workbook.close()

    print(df)
    print(ds)

    ds.plot()
    plt.show()

sid="^BSESN"
name="sensex"
stock(sid, name)

print("Please run sqlmod")
