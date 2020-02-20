import tkinter as t
import Igbot

root=t.Tk()
root.configure(background='light blue')
root.title('InstaGram')
root.iconbitmap(r'.\insta.ico')
root.geometry('450x450')
root.resizable(width=True, height=True)

t1=t.Label(root,text="User Name: ",font=(16),bg='light blue')
t1.place(x=40,y=102)
t2=t.Label(root,text="Password: ",font=(16),bg='light blue')
t2.place(x=40,y=152)

t3=t.Label(root,text="Unfollow No: ",font=(16),bg='light blue')
t3.place(x=40,y=202)

global ue1
ue1=t.Entry(root,width=30)
ue1.place(x=200,y=105)

global ue2
ue2=t.Entry(root,show="*",width=30)
ue2.place(x=200,y=155)

global ue3
ue3=t.Entry(root,width=30)
ue3.place(x=200,y=205)
def boo():
    uname = str(ue1.get())
    passw = str(ue2.get())
    unno = int(ue3.get())
    Igbot.Instagram(uname,passw,unno)

sb1=t.Button(root,text="Login",font=("bold",10),width=(15),bg="light blue",command=boo)
sb1.place(x=200,y=250)


root.mainloop()