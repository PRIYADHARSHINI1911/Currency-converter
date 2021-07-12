from tkinter import *

window = Tk()
window.configure(background='#242B2E')
window.title("Dollar to Rupees")
window.iconbitmap('favicon.ico')

def conversion():
    indianrupees=float(dollars.get())*75
    t1.delete("1.0",END)
    t1.insert(END,indianrupees)

b1=Button(window,text="Convert",command=conversion)
b1.grid(row=3,column=1,pady=10,padx=20)
b1.configure(background='#50DBB4')

dollars=StringVar()
e1 = Entry(window,textvariable=dollars)
e1.grid(row=2,column=1,pady=10,padx=20)

t1=Text(window,height=2,width=10)
t1.grid(row=4,column=1,pady=10,padx=20)
window.mainloop()
