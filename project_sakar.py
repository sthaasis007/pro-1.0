from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
scr = Tk()
scr.title("Hospital DB")   # for title name 
# scr.iconbitmap('C:\\Users\\Accer\\Desktop\\project\\Hospi.ico') # for putting icon should be .ico file
scr.geometry('900x500')     #for hight and weight
scr.resizable(False,TRUE)
# pic=PhotoImage(file="C:\\Users\\Accer\\Desktop\\project\\Ho.png")
# Label(scr,image=pic).place(x=50,y=0)
scr.config(bg='gray')
dis=Label(scr,text='Hospital Management System',bg='white',font=('Mycrosoft YaHei UI Light',40,'bold')).pack()

def press():
    scr.destroy()
    import fpage

press=Button(scr,text="Click me",border=0,fg="red",font=('Micrsoft YaHei UI Light',10,'bold'),command=press).place(x=430,y=295)

scr.mainloop()