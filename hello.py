from tkinter import*
from tkinter import messagebox
import sqlite3

root=Tk()
lbl=Label(root,text='employe management system',font=('Arial Bold',50))
lbl.place(x=200,y=0)
root.geometry('1300x650')
root.resizable(0,0)
root.config(bg='light gray')

def add():
    conn=sqlite3.connect('gender_database.db')
    c=conn.cursor()
    c.execute("INSERT INTO employee(name,adrs,rol,slry) VALUES(?,?,?,?)"
              ,(username.get(),address.get(),role.get(),salary.get()))
    conn.commit()
    conn.close()
    username.delete(0,END)
    address.delete(0,END)
    role.delete(0,END)
    salary.delete(0,END)

def retrive():
    conn=sqlite3.connect("gender_database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM employee')
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

def delete():
    conn=sqlite3.connect("gender_database.db")
    c=conn.cursor()
    c.execute("DELETE FROM employee WHERE ID="+delete_box.get())
    conn.commit()
    conn.close()
    delete_box.delete(0,END)
    retrive()

def update(record_id):
    conn=sqlite3.connect("gender_database.db")
    c=conn.cursor()
    c.execute("""
              UPDATE employee SET 
              uname = :u,
              adr = :a
              rl = :r
              slr = :s
              WHERE ID = :id""",
              {
                  'u': username_editor.get(),
                  'a': address_editor.get(),
                  'r': role_editor.get(),
                  's': salary_editor.get(),
                  'id': record_id
              }
    )
    conn.commit()
    conn.close()


def edit():
    global editor
    editor=Tk()
    editor.title('Update Data')
    editor.geometry('300x480')
    conn=sqlite3.connect('gender_database.db')
    c=conn.cursor()
    record_id=update_box.get()
    c.execute("SELECT * FROM employee WHERE ID=?",(record_id,))
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

    # create text box labels
    username_label=Label(editor,text="Username")
    username_label.grid(row=0 ,column=0 ,pady=(10,0))

    address_label=Label(editor,text="Address")
    address_label.grid(row=1 ,column=0)

    role_label=Label(editor,text="Role")
    role_label.grid(row=2 ,column=0 )

    salary_label=Label(editor,text="salary")
    salary_label.grid(row=3 ,column=0 )

    for record in records:
        username_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        role_editor.insert(0,record[3])
        salary_editor.insert(0,record[3])

    update_box.delete(0,END)
    edit_btn=Button(editor,text="Save")
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=125)
    conn.close()




label_username=Label(root,text='username',font=('Arial Bold',20))
label_username.place(x=0,y=90)

label_address=Label(root,text='addres',font=('Arial Bold',20))
label_address.place(x=0,y=140)

label_role=Label(root,text='role',font=('Arial Bold',20))
label_role.place(x=0,y=190)

label_salary=Label(root,text='salary',font=('Arial Bold',20))
label_salary.place(x=0,y=240)

label_delete=Label(root,text='delete_data',font=('Arial Bold',20))
label_delete.place(x=0,y=370)

label_updet=Label(root,text='Update_data',font=('Arial Bold',20))
label_updet.place(x=0,y=440)

update_box=Entry(root,width=25)
update_box.place(x=210,y=440,height=30)

address=Entry(root,width=30)
address.place(x=170,y=150,height=30)

role=Entry(root,width=30)
role.place(x=170,y=200,height=30)

salary=Entry(root,width=30)
salary.place(x=170,y=250,height=30)

delete_box=Entry(root,width=25)
delete_box.place(x=210,y=370,height=30)

username=Entry(root,width=30)
username.place(x=170,y=100,height=30)

btn_add=Button(root,text='Add',font=('Arial Bold',20),command=add)
btn_add.place(x=0,y=300)

btn_retrive=Button(root,text='Retrive',font=('Arial Bold',20),command=retrive)
btn_retrive.place(x=100,y=300)

btn_delete=Button(root,text='Delete',font=('Arial Bold',20),command=delete)
btn_delete.place(x=380,y=350)

update_btn=Button(root, text="Update",font=('Arial Bold',20),command=edit)
update_btn.place(x=380,y=420)

conn=sqlite3.connect('gender_database.db')
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employee(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               name             TEXT,
               adrs             TEXT,
               rol              TEXT,
               slry             INT
)""")
conn.commit()
conn.close()






root.mainloop()