
from tkinter import*
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('Patient Form')
root.state('zoomed')
root.config(bg='light gray')
root.iconbitmap('C:\\Users\\Accer\\Desktop\\project\\Hospi.ico')
docimg=PhotoImage(file="C:\\Users\\Accer\\Desktop\\project\\ptbg.png")
Label(root,image=docimg).place(x=-150,y=0)
lbl=Label(root,text='Patient',bg='light blue',font=('Arial Bold',50)).pack()

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS ptrc(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name             TEXT,
            dies             TEXT,
            rom              INT,
            bed             INT
)""")


frame=Frame(root,width=350,height=400,bg="light gray")
frame.place(x=500,y=160)

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
role.insert(1,"Room No.")
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

def on_enter(e):
    delete_box.delete(0,'end')

def on_leave(e):
    name=delete_box.get()
    if name=='':
        delete_box.insert(0,'Delete ')

delete_box=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
delete_box.place(x=30,y=250)
delete_box.insert(0,"Delete Entry")
delete_box.bind('<FocusIn>',on_enter)
delete_box.bind('<FocusOut>',on_leave)

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
btn_add.place(x=10,y=300)

def retrive():
    conn=sqlite3.connect("hospital.db")
    c = conn.cursor()
    c.execute('SELECT * FROM ptrc')
    records=c.fetchall()
    # print(records)
    print_record=''
    for record in records:
        print_record += str(record[0])+' '+\
        str(record[1])+' '+str(record[2])+' '+str(record[3]) +\
        ' '+str(record[4])+"\n"
    query_label=Label(root,text=records)
    query_label.place(x=560,y=90)
    conn.close()

btn_retrive=Button(frame,width=10,text='Retrive',bg='blue',font=8,fg='white',border=0,command=retrive)
btn_retrive.place(x=125,y=300)

def delete():
    conn=sqlite3.connect("hospital.db")
    c=conn.cursor()
    c.execute("DELETE FROM ptrc WHERE ID="+delete_box.get())
    conn.commit()
    conn.close()
    delete_box.delete(0,END)
    retrive()

btn_delete=Button(frame,width=10,text='Delete',bg='blue',font=8,fg='white',border=0,command=delete)
btn_delete.place(x=240,y=300)

def edit():
    global editor
    editor=Tk()
    editor.iconbitmap('C:\\Users\\Accer\\Desktop\\project\\Hospi.ico')
    editor.title('Update Data')
    editor.geometry('300x400')
    con=sqlite3.connect('hospital.db')
    c=con.cursor()
    record_id=updatebox.get()
    c.execute('SELECT * FROM ptrc WHERE ID=?',(record_id,))
    records=c.fetchall()
    global username_editor
    global address_editor
    global role_editor
    global salary_editor

    username_editor=Entry(editor,width=30)
    username_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=1,column=1)

    role_editor=Entry(editor,width=30)
    role_editor.grid(row=2,column=1)

    salary_editor=Entry(editor,width=30)
    salary_editor.grid(row=3,column=1)
    
    username_label=Label(editor,text="Patient Name")
    username_label.grid(row=0,column=0,pady=(10,0))

    address_label=Label(editor,text="Diesease")
    address_label.grid(row=1,column=0)

    role_label=Label(editor,text="Room no.")
    role_label.grid(row=2,column=0)

    salary_label=Label(editor,text="Bed no.")
    salary_label.grid(row=3,column=0)

    for record in records:
        username_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        role_editor.insert(0,record[3])
        salary_editor.insert(0,record[4])

    updatebox.delete(0,END)
    btn_save=Button(editor,text='SAVE',command=lambda:update(record_id))
    btn_save.grid(row=5,column=0,columnspan=2, pady=10,padx=10,ipadx=125)
    

def update(record_id):
    con=sqlite3.connect('hospital.db')
    c=con.cursor()
    c.execute('''
        UPDATE ptrc SET 
            name=:u,
            dies=:a,
            rom=:r,
            bed=:s
            WHERE ID = :id''',
            {
                'u': username_editor.get(),
                'a': address_editor.get(),
                'r': role_editor.get(),
                's': salary_editor.get(),
                'id': record_id
            }
    )
    con.commit()
    con.close()
    editor.destroy()
    # retrieve()

def on_enter(e):
    updatebox.delete(0,'end')

def on_leave(e):
    name=updatebox.get()
    if name=='':
        updatebox.insert(0,'Update Entry (Id) ')

updatebox=Entry(frame,width=15,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
updatebox.place(x=30,y=340,height=30)
updatebox.insert(0,"Update Entry (Id)")
updatebox.bind('<FocusIn>',on_enter)
updatebox.bind('<FocusOut>',on_leave)


btn_edit=Button(frame,width=15,text='Update Records',bg='blue',font=8,fg='white',border=0,command=edit)
btn_edit.place(x=170,y=340)


def bck():
    root.destroy()
    import fpage


back=Button(root,text="<== Back",font=('Arial Bold',10),command=bck).place(x=0,y=10)


root.mainloop()