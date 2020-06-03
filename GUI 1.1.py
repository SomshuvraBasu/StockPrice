from tkinter import *
import mysql.connector as m
import tkinter.messagebox as mb

a=Tk()
a.resizable(0,0)
#a.wm_attributes('-transparentcolor','white')
a.geometry('900x550')
a.title("I8PI Digital Solutions")
a.iconphoto(False, PhotoImage(file="E:\Computer Science\Images\spiral.png"))
imag=PhotoImage(file="E:\Computer Science\Images\stock.png")
b=Label(a, image=imag,width=950,height=550).pack()

def insert():
    stock_name=na.get()
    start=nu.get()
    end=da.get()
    
    if (stock_name=='' or start=='' or end==''):
        mb.showinfo(' ',"   All fields are to be filled   ")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="1234",database="stock")
        mycursor=mydb.cursor()
        mycursor.execute("insert into acchold values('"+stock_name+"','"+start+"','"+end+"','"+ifsccode+"','"+balance+"','"+pstcode+"')")
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

'''
def show():
    if (nu.get()==''):
        mb.showinfo("","All fields are to be filled")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="123",database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("select * from acchold where accname='"+nu.get()+"'")
        r=mycursor.fetchall()

        for i in r:
            na.insert(0,i[1])
            da.insert(1,i[5])
            co.insert(5,i[3])
            i.insert(3,i[4])
            z.insert(4,i[5])

        mydb.close()
'''
'''
def update():
    if (nu.get()==''):
        mb.showinfo('',"Account Number is compulsory for update")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="123",database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("update acchold set accname='"+accname+"',end='"+end+"',ifsccode='"+ifsccode+"',balance='"+balance+"',pstcode='"+pstcode+"' where start='"+nu.get()+"'")
        mycursor.execute('commit')

    mydb.commit()
    na.delete(0,'end')
    nu.delete(0,'end')
    da.delete(0,'end')
    co.delete(0,'end')
    i.delete(0,'end')
    z.delete(0,'end')
    mb.showinfo('',"Values are updated")
    mydb.close()
'''

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

form=Label(a, text="STOCK MARKET OBSERVER", width=35, font=("bold",15)).place(x=250,y=20)

Checkbutton(a, text="Is It A Index", variable=var1, font=("underline",10), width=18).place(x=280,y=100)

stock_n=Label(a, text="Index Name Of Stock", width=20, font=("Times 32",10), padx=5, pady=2).place(x=280,y=150)

start=Label(a, text="Enter Start Date", width=20, font=("Times 32",10), padx=5, pady=2).place(x=280,y=225)

end=Label(a, text="Enter End Date", width=20, font=("Times 32",10), padx=5, pady=2).place(x=280,y=300)

na=Entry(relief=SOLID)
na.place(x=500,y=150)

nu=Entry(relief=SOLID)
nu.place(x=500,y=225)

da=Entry(relief=SOLID)
da.place(x=500,y=300)

insert=Button(a,text="Submit",width=20,bg="grey",fg="black",command=insert).place(x=250,y=450)

delete=Button(a,text="Delete",width=20,bg="grey",fg="black",command=delete).place(x=352,y=500)

cl=Button(a,text="Clear",width=20,bg="grey",fg="black",command=clear).place(x=455,y=450)

a.mainloop()