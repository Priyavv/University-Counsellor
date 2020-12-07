from tkinter import *
from tkinter import ttk

import sqlite3
connection=sqlite3.connect("login.db")
cursor=connection.cursor()

t=Tk()
t.title("tk")

l1=ttk.Label(t,text="Username")
l1.grid(row=0,column=0)
t1=Entry(t)
t1.grid(row=0,column=1)
a=t1.get()

l2=ttk.Label(t,text="Password")
l2.grid(row=1,column=0)
t2=Entry(t)
t2.grid(row=1,column=1)
b=t2.get()

l3=ttk.Label(t,text="Contact")
l3.grid(row=2,column=0)
t3=Entry(t)
t3.grid(row=2,column=1)
c=t3.get()

l4=ttk.Label(t,text="Email")
l4.grid(row=3,column=0)
t4=Entry(t)
t4.grid(row=3,column=1)
d=t4.get()

b1=Button(t,text="Login")
b1.grid(row=4,column=1)

def create_table():
    cursor.execute("create table if not exists login(username TEXT, password TEXT, contact INTEGER, email TEXT)")
    cursor.execute("INSERT INTO login VALUES (?,?,?,?)",t1.get(),t2.get(),t3.get,t4.get())
    connection.commit()

b1=ttk1.Button(t,text="LOGIN",command=create_table)
b1.grid(row=4,column=1,columnspan=2)

t.mainloop()
