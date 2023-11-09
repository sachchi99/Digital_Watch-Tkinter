from tkinter import *
from tkinter.ttk import *
import datetime as dt
from time import strftime

root=Tk()
root.title('Digital-Clock')
root.geometry("550x200")
root.configure(bg="#2C3C3F")
def time():
    st=strftime('%I:%M:%S %p')
    lbl.config(text=st)
    lbl.after(1000, time)
lbl=Label(root, font=('radioland', 60, 'bold'), background='#2C3C3F', foreground='#00D2FF')
lbl.pack(anchor='center')
time()

date = dt.datetime.now()
label = Label(root, text=f"{date:%A, %B %d, %Y}", font=('radioland', 17, 'bold'), background='#2C3C3F', foreground='#00D2FF')
label.pack(pady=20)

mainloop()