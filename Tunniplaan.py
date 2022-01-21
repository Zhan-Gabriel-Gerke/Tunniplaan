from tkinter import*
from tkinter.messagebox import*
root=Tk()
root.title("Эти загадочные числа")
root.geometry("1500x800+100+100")
root.resizable(width=False, height=False)
 
def outTextEestikeel():
  label.configure(text="Hello!")
def outTextLogistika():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")
def outText():
  label.configure(text="Hello!")


btn1 = Button(root, command=outText, text="Числа", background="#008000", foreground="#fff", pady="2", font="12", width=30)
btn1.place(x=10,y=20)
label = Label(root)
label.place(x=700, y=600)
Button(text="         ",font="Arial 15").grid(row=0,column=0)
Button(text="Esmaspäev",relief="flat",font="Arial 15").grid(row=1,column=0)
Button(text="Teisipäev",relief="flat",font="Arial 15").grid(row=2,column=0)
Button(text="Kolmapäev",relief="flat",font="Arial 15").grid(row=3,column=0)
Button(text="Neljapäev",relief="flat",font="Arial 15").grid(row=4,column=0)
Button(text="Reede",relief="flat",font="Arial 15").grid(row=5,column=0)
Button(text="0",relief="flat",font="Arial 15").grid(row=0,column=1)
Button(text="1",relief="flat",font="Arial 15").grid(row=0,column=2)
Button(text="2",relief="flat",font="Arial 15").grid(row=0,column=3)
Button(text="3",relief="flat",font="Arial 15").grid(row=0,column=4)
Button(text="4",relief="flat",font="Arial 15").grid(row=0,column=5)
Button(text="5",relief="flat",font="Arial 15").grid(row=0,column=6)
Button(text="6",relief="flat",font="Arial 15").grid(row=0,column=7)
Button(text="7",relief="flat",font="Arial 15").grid(row=0,column=8)
Button(text="8",relief="flat",font="Arial 15").grid(row=0,column=9)
Button(text="9",relief="flat",font="Arial 15").grid(row=0,column=10)
Button(text="10",relief="flat",font="Arial 15").grid(row=0,column=11)
Button(text="Eestikeel Tugiõpe",bg="#6c6e6a",relief="flat",font="Arial 15",width=15,height=3).grid(row=1,column=2,sticky=W+E+N+S)
Button(text="Logistika",bg="#59ff00",relief="flat",font="Arial 15",width=30,height=3).grid(row=1,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="Matematika",bg="#fb00ff",relief="flat",font="Arial 15",width=30,height=3).grid(row=1,column=5,columnspan=2,sticky=W+E+N+S)
Button(text="Перерыв",font="Arial 15",width=15,height=3).grid(row=1,column=7,)
Button(text="Venekell",bg="#60ad36",relief="flat",font="Arial 15",width=30,height=3).grid(row=1,column=8,columnspan=2,sticky=W+E+N+S)
Button(text="Matemaatika Tugiõpe",bg="#fb00ff",relief="flat",font="Arial 15",width=15,height=3).grid(row=1,column=10,sticky=W+E+N+S)
Button(text="Keemia Tugiõpe",bg="#912f2f",relief="flat",font="Arial 15",width=15,height=3).grid(row=2,column=2,sticky=W+E+N+S)
Button(text="Програмирование",bg="#2f8491",relief="flat",font="Arial 15",width=45,height=3).grid(row=2,column=3,columnspan=3,sticky=W+E+N+S)
Button(text="Перерыв",font="Arial 15",width=15,height=3).grid(row=2,column=6)
Button(text="Füüsika",bg="#fb00ff",relief="flat",font="Arial 15",width=30,height=3).grid(row=2,column=7,columnspan=2,sticky=W+E+N+S)
Button(text="Inglisekeel",bg="#fb00ff",relief="flat",font="Arial 15",width=15,height=3).grid(row=3,column=2,sticky=W+E+N+S)
Button(text="Kunst",bg="#912f2f",relief="flat",font="Arial 15",width=30,height=3).grid(row=3,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="Перерыв",font="Arial 15",width=15,height=3).grid(row=3,column=5)
Button(text="физра",bg="#912f2f",relief="flat",font="Arial 15",width=30,height=3).grid(row=3,column=6,columnspan=2,sticky=W+E+N+S)
Button(text="Logistika",bg="#59ff00",relief="flat",font="Arial 15",width=30,height=3).grid(row=4,column=2,columnspan=2,sticky=W+E+N+S)
Button(text="Перерыв",font="Arial 15",width=15,height=3).grid(row=4,column=4)
Button(text="Програмирование",bg="#2f8491",relief="flat",font="Arial 15",width=30,height=3).grid(row=4,column=5,columnspan=2,sticky=W+E+N+S)
Button(text="Rakendus",bg="#9e0e0e",relief="flat",font="Arial 15",width=30,height=3).grid(row=4,column=7,columnspan=2,sticky=W+E+N+S)
Button(text="Eestikeel",bg="#6c6e6a",relief="flat",font="Arial 15",width=30,height=3).grid(row=4,column=9,columnspan=2,sticky=W+E+N+S)
Button(text="Rakendus",bg="#9e0e0e",relief="flat",font="Arial 15",width=30,height=3).grid(row=5,column=2,columnspan=2,sticky=W+E+N+S)
Button(text="Програмирование",bg="#2f8491",relief="flat",font="Arial 15",width=80,height=3).grid(row=5,column=4,columnspan=5,sticky=W+E+N+S)
Button(text="Inglisekeel",bg="#60ad36",relief="flat",font="Arial 15",width=30,height=3).grid(row=5,column=9,columnspan=2,sticky=W+E+N+S)
root.mainloop()