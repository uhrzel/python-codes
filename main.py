#ok lets create a simple calculator

from tkinter import *

root = Tk()
root.title("Simple Calculator")

def one():
    entry1.config(state="normal")
    entry1.insert(END,str(1))
    entry1.config(state="readonly")
def two():
    entry1.config(state="normal")
    entry1.insert(END,str(2))
    entry1.config(state="readonly")
def three():
    entry1.config(state="normal")
    entry1.insert(END,str(3))
    entry1.config(state="readonly")
def four():
    entry1.config(state="normal")
    entry1.insert(END,str(4))
    entry1.config(state="readonly")
def five():
    entry1.config(state="normal")
    entry1.insert(END,str(5))
    entry1.config(state="readonly")
def six():
    entry1.config(state="normal")
    entry1.insert(END,str(6))
    entry1.config(state="readonly")
def seven():
    entry1.config(state="normal")
    entry1.insert(END,str(7))
    entry1.config(state="readonly")
def eight():
    entry1.config(state="normal")
    entry1.insert(END,str(8))
    entry1.config(state="readonly")
def nine():
    entry1.config(state="normal")
    entry1.insert(END,str(9))
    entry1.config(state="readonly")
def zero():
    entry1.config(state="normal")
    entry1.insert(END,str(0))
    entry1.config(state="readonly")
def dot():
    entry1.config(state="normal")
    entry1.insert(END,".")
    entry1.config(state="readonly")
def summ():
    entry1.config(state="normal")
    entry1.insert(END,"+")
    entry1.config(state="readonly")
def minus():
    entry1.config(state="normal")
    entry1.insert(END,"-")
    entry1.config(state="readonly")
def multiplication():
    entry1.config(state="normal")
    entry1.insert(END,"x")
    entry1.config(state="readonly")
def divide():
    entry1.config(state="normal")
    entry1.insert(END,"÷")
    entry1.config(state="readonly")
def percentage():
    entry1.config(state="normal")
    current_value = float(entry1.get())
    percent_value = current_value / 100
    entry1.delete(0, END)
    entry1.insert(END, str(percent_value))
    entry1.config(state="readonly")
def clear_entry():
    entry1.config(state="normal")
    entry1.delete(0, END)
    entry1.config(state="readonly")
def remove_char():
    entry1.config(state="normal")
    current_text = entry1.get()
    new_text = current_text[:-1]  
    entry1.delete(0, END)
    entry1.insert(END, new_text)
    entry1.config(state="readonly")
def result():
    primary_result = entry1.get()
    final_result = eval(primary_result.replace("x", "*").replace("÷", "/"))
    entry1.config(state="normal")
    entry1.delete(0, END)
    entry1.insert(END, "=" + str(final_result))
    entry1.config(state="readonly")

button_width = 5

btnc = Button(root,text="©",padx=10,pady=10,width=button_width,command=clear_entry)
btnc.grid(row=1,column=0,sticky="snew")

btndiv = Button(root,text="➗",padx=10,pady=10,width=button_width,command=divide)
btndiv.grid(row=1,column=1,sticky="snew")

btntimes = Button(root,text="✖️",padx=10,pady=10,width=button_width,command=multiplication)
btntimes.grid(row=1,column=2,sticky="snew")

btndel = Button(root,text="⌫", font="bold",padx=10,pady=10,width=button_width,command=remove_char)
btndel.grid(row=1,column=3,sticky="snew")


btnseven = Button(root,text="7",padx=10,pady=10,width=button_width,command=seven)
btnseven.grid(row=2,column=0,sticky="snew")

btneight = Button(root,text="8",padx=10,pady=10,width=button_width,command=eight)
btneight.grid(row=2,column=1,sticky="snew")

btnnine = Button(root,text="9",padx=10,pady=10,width=button_width,command=nine)
btnnine.grid(row=2,column=2,sticky="snew")

btnsum = Button(root, text="➕", width=button_width, padx=10, pady=10, bg="blue",command=summ)
btnsum.grid(row=2, column=3 , sticky="nsew")


btnfour = Button(root,text="4",padx=10,pady=10,width=button_width,command=four)
btnfour.grid(row=3,column=0,sticky="snew")

btnfive = Button(root,text="5",padx=10,pady=10,width=button_width,command=five)
btnfive.grid(row=3,column=1,sticky="snew")

btnsix = Button(root,text="6",padx=10,pady=10,width=button_width,command=six)
btnsix.grid(row=3,column=2,sticky="snew")

btnsub = Button(root, text="➖", width=button_width, padx=10, pady=10, bg="blue",command=minus)
btnsub.grid(row=3, column=3 , sticky="nsew")


btnone = Button(root,text="1",padx=10,pady=10,width=button_width,command=one)
btnone.grid(row=4,column=0,sticky="snew")

btntwo = Button(root,text="2",padx=10,pady=10,width=button_width,command=two)
btntwo.grid(row=4,column=1,sticky="snew")

btnthree = Button(root, text="3", width=button_width, padx=10, pady=10,command=three)
btnthree.grid(row=4, column=2 , sticky="nsew")

btnequal = Button(root, text="=", width=button_width, padx=10, pady=10, bg="green", command=result)
btnequal.grid(row=4, column=3, sticky="nsew")



btnave = Button(root,text="%",padx=10,pady=10,width=button_width,command=percentage)
btnave.grid(row=5,column=0,sticky="snew")

btnzero = Button(root,text="0",padx=10,pady=10,width=button_width,command=zero)
btnzero.grid(row=5,column=1,sticky="snew")

btndot = Button(root, text=".", width=button_width, padx=10, pady=10,command=dot)
btndot.grid(row=5, column=2 , sticky="nsew")


entry1 = Entry(state="readonly")
entry1.grid(row=0, column=0, sticky="nsew", pady=20,padx=20)

root.grid_columnconfigure(0, weight=1, uniform="buttons")
root.grid_columnconfigure(1, weight=1, uniform="buttons")
root.grid_columnconfigure(2, weight=1, uniform="buttons")
root.grid_columnconfigure(3, weight=1, uniform="buttons")
root.mainloop()