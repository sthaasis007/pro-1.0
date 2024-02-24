from tkinter import*
from tkinter import messagebox


win=Tk()
win.title("Welcome")
win.state('zoomed')
# win.iconbitmap('C:\\Users\\Accer\\Desktop\\project\\Hospi.ico')
# pic=PhotoImage(file='C:\\Users\\Accer\\Desktop\\project\\Img2.png')
# Label(win,image=pic).pack()

def doc():
    win.destroy()
    import Doc

frame=Frame(win,width=350,height=100,bg="gray")
frame.place(x=200,y=150)
lblford=Label(frame,text="For Doctor info",bg='gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=100,y=10)
doc=Button(frame,width=30,text='Doc',bg='blue',font=8,fg='white',border=0,command=doc).place(x=40,y=50)

def reg():
    win.destroy()
    import reg
frame=Frame(win,width=350,height=100,bg="dark gray")
frame.place(x=650,y=150)
lblford=Label(frame,text='Registration',bg='dark gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=110,y=10)
doc=Button(frame,width=30,text='Reg',bg='blue',font=8,fg='white',border=0,command=reg).place(x=40,y=50)

def ptr():
    win.destroy()
    import ptrc

frame=Frame(win,width=350,height=100,bg="dark gray")
frame.place(x=200,y=400)
lblforc=Label(frame,text="For Patient report info",bg='dark gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=70,y=10)
doc=Button(frame,width=30,text='Report',bg='blue',font=8,fg='white',border=0,command=ptr).place(x=40,y=50)


def stf():
    win.destroy()
    import stf
frame=Frame(win,width=350,height=100,bg="gray")
frame.place(x=650,y=400)
lblford=Label(frame,text="Staff Info",bg='gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=120,y=10)
doc=Button(frame,width=30,text='Staff',bg='blue',font=8,fg='white',border=0,command=stf).place(x=40,y=50)

win.mainloop()