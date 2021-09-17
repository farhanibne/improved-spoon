from tkinter import *
import os

def shutdown():
    return os.system("shutdown /s /t l")

def restart():
    return os.system("shutdown /r /t l")

master = Tk()
master.geometry("600x400")

master.configure(bg='light grey')

Button(master,text="Shut Down",command=shutdown).place(x=250,y=200)
Button(master, text="Restart", command=restart).place(x=255,y=250)


mainloop()