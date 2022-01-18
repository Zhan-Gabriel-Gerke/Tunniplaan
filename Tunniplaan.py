from tkinter import *
root=Tk()

lable_(text="Имя").grid(row=0,column=0)
table_name = Entry(width=30)
table_name.grid(row=0, column=1, columnspan=3)

Lable (text="столбцов").grid(row=1,column=0)
table_column = spinbox(width=7, from_1, to=50)
table_column.grid(row=1, column=1)

Lable (text="строк").grid(row=1,column=2)
table_column = spinbox(width=7, from_1, to=100)
table_column.grid(row=1, column=3)
 
button(text="справка").grid(row=2, column=0)
button(text="вставить").grid(row=2, column=2)
button(text="отменить").grid(row=2, column=3)

root.mainloop()