from tkinter import *
import time


window=Tk()
window.title("Digital Clock")
window.geometry('600x500')
def mytime():
    hour=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    am_pm=time.strftime("%p")

    day=time.strftime("%A")
    zone=time.strftime("%Z")

    myhour=hour+":"+min+":"+sec+""+am_pm
    mylabel.config(text=myhour)
    mylabel.after(1000,mytime)

    myday=day+"  "+zone
    mylabel2.config(text=myday)
    

mylabel=Label(window,text="hello word",font=('Arial',72),fg="white",bg="pink")
mylabel.pack()
mylabel2=Label(window,text="",font=("Arial",54),fg="pink",bg="white")
mylabel2.pack()
mytime()

window.mainloop()