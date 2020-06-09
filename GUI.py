from tkinter import *
import mysql.connector as m
import tkinter.messagebox as mb

def loop():

    a=Tk()
    a.resizable(0,0)
    #a.wm_attributes('-transparentcolor','white')
    a.geometry('900x550')
    a.title("I8PI Digital Solutions")
    a.iconphoto(False, PhotoImage(file="E:\Computer Science\Images\logo.png"))
    imag=PhotoImage(file="E:\Computer Science\Images\stock.png")
    b=Label(a, image=imag,width=950,height=550).pack()

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
    sid=StringVar()
    name=StringVar()


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

    cl=Button(a,text="Clear",width=20,bg="grey",fg="black",command=clear).place(x=455,y=450)

    a.mainloop()

    #print(sid)
   
