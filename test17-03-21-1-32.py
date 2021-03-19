from tkinter import *
import tkinter as tk
#from PIL import Image, ImageTk

gui = Tk()
gui.option_add("*Font", "courier 20")
gui.minsize(width=700,height=500)
gui.title("โปรแกรมกู้เงินพอมเจมส์")

Label (gui,text="กรุณาเลือกกดตัวเลือกต่อไปนี้",bg='red3').pack(fill=X)
Button (gui,text ="สมัครสมาชิก").place(relx=0.05,rely=0.2)
Button (gui,text ="เข้าสู่ระบบ").place(relx=0.05,rely=0.36)
Button (gui,text ="ออกจากโปรแกรม").place(relx=0.05,rely=0.85)

photo = PhotoImage(file="POK.jpg")
Label (gui, image=photo, borderwidth=0).pack()

gui.mainloop()