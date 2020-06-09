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

if os.path.exists("StockPrices.xlsx"):
    os.remove("StockPrices.xlsx")
else:
    pass

a=Tk()
a.resizable(0,0)
#a.wm_attributes('-transparentcolor','white')
a.geometry('900x550')
a.title("I8PI Digital Solutions")
a.iconphoto(False, PhotoImage(file="E:\Computer Science\Images\logo.png"))
imag=PhotoImage(file="E:\Computer Science\Images\stock.png")
b=Label(a, image=imag,width=950,height=550).pack()

def submit():
    stock_name=na.get()
    start=nu.get()
    end=da.get()
    
    if (stock_name=='' or start=='' or end==''):
        mb.showinfo(' ',"   All fields are to be filled   ")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="1234",database="stock")
        mycursor=mydb.cursor()
        mycursor.execute("insert into acchold values('"+stock_name+"','"+start+"','"+end+")")
        mycursor.execute('commit')

    mydb.commit()
    na.delete(0,'end')
    nu.delete(0,'end')
    da.delete(0,'end')
    mb.showinfo("","Values are inserted")
    mydb.close()


def delete():
    if (nu.get()==''):
        mb.showinfo("","All fields are to be filled")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="123",database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("delete from acchold where accname='"+nu.get()+"'")
        mycursor.execute('commit')

    mydb.commit()
    na.delete(0,'end')
    nu.delete(0,'end')
    da.delete(0,'end')
    co.delete(0,'end')
    i.delete(0,'end')
    z.delete(0,'end')
    mb.showinfo("","Values are deleted")
    mydb.close()

def sub():
    a.destroy()

def clear():
    na.delete(0, END)
    nu.delete(0, END)
    da.delete(0, END)
    '''
    co.delete(0, END)
    i.delete(0, END)
    z.delete(0, END)
    a.configure(state='normal')
    '''

var1 = IntVar()
#sid=StringVar()
#name=StringVar()


form=Label(a, text="STOCK MARKET OBSERVER", width=35, font=("bold",15)).place(x=250,y=20)

Checkbutton(a, text="Is It A Index", variable=var1, font=("underline",10), width=18).place(x=280,y=100)

stock_n=Label(a, text="Index Name Of Stock", width=20, font=("Times 32",10), padx=5, pady=2)
stock_n.place(x=280,y=150)

start=Label(a, text="Enter Start Date", width=20, font=("Times 32",10), padx=5, pady=2).place(x=280,y=225)

namestock=Label(a, text="Enter Stock Name", width=20, font=("Times 32",10), padx=5, pady=2)
namestock.place(x=280,y=300)

na=Entry(relief=SOLID)
na.place(x=500,y=150)

nu=Entry(relief=SOLID)
nu.place(x=500,y=225)

da=Entry(relief=SOLID)
da.place(x=500,y=300)

sub=Button(a,text="Submit",width=20,bg="grey",fg="black",command=sub).place(x=250,y=450)

delete=Button(a,text="Delete",width=20,bg="grey",fg="black",command=delete).place(x=352,y=500)

cl=Button(a,text="Clear",width=20,bg="grey",fg="black",command=clear).place(x=455,y=450)

a.mainloop()

sid=na.get()
name=da.get()

print(sid)
print(name)

'''
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
    ws.write(row, col + 2, '90Moving')

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


stock(sid, name)

'''
