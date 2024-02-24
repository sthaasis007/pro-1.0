
from tkinter import*
from tkinter import messagebox
import sqlite3

root=Tk()
root.state('zoomed')
root.config(bg='light gray')
root.iconbitmap('C:\\Users\\Accer\\Desktop\\project\\Hospi.ico')
root.title('Regrestration')
docimg=PhotoImage(file="C:\\Users\\Accer\\Desktop\\project\\hobgr.png")
Label(root,image=docimg).place(x=0,y=0)
lbl=Label(root,text='Register',bg='light gray',font=('Arial Bold',50)).pack()

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS ptrc(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name             TEXT,
            dies             TEXT,
            rom              INT,
            bed             INT
)""")

frame=Frame(root,width=350,height=350,bg="light gray")
frame.place(x=500,y=180)

lbl=Label(frame,text="Enter patient details",bg="light gray",font=('Microsoft YaHei UI Light',15,'bold'))
lbl.place(x=50,y=10)

def on_enter(e):
    username.delete(0,'end')

def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,'Patient Name')
        
username=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
username.place(x=30,y=50,height=30)
username.insert(0,"Patient Name")
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave)

def on_enter(e):
    address.delete(0,'end')

def on_leave(e):
    name=address.get()
    if name=='':
        address.insert(0,'Diagnosed With')

address=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
address.place(x=30,y=100,height=30)
address.insert(0,"Diagnosed With")
address.bind('<FocusIn>',on_enter)
address.bind('<FocusOut>',on_leave)

def on_enter(e):
    role.delete(0,'end')

def on_leave(e):
    name=role.get()
    if name=='':
        role.insert(0,'Room No.')

role=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
role.place(x=30,y=150,height=30)
role.insert(0,"Room No.")
role.bind('<FocusIn>',on_enter)
role.bind('<FocusOut>',on_leave)

def on_enter(e):
    salary.delete(0,'end')

def on_leave(e):
    name=salary.get()
    if name=='':
        salary.insert(0,'Bed No.')

salary=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
salary.place(x=30,y=200,height=30)
salary.insert(0,"Bed No.")
salary.bind('<FocusIn>',on_enter)
salary.bind('<FocusOut>',on_leave)

def add():
    conn=sqlite3.connect('hospital.db')
    c=conn.cursor()
    c.execute("INSERT INTO ptrc(name,dies,rom,bed) VALUES(?,?,?,?)"
            ,(username.get(),address.get(),role.get(),salary.get()))
    conn.commit()
    conn.close()
    username.delete(0,END)
    address.delete(0,END)
    role.delete(0,END)
    salary.delete(0,END)

btn_add=Button(frame,width=10,text='Add',bg='blue',font=8,fg='white',border=0,command=add)
btn_add.place(x=120,y=250)


def bck():
    root.destroy()
    import fpage

back=Button(root,text="<== Back",font=('Arial Bold',10),command=bck).place(x=0,y=10)


root.mainloop()