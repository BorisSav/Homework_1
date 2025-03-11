from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from math import *

def summ(b):
    a = calc.get()
    if a[0]=='0' and len(a)==1:
        a = a[1:]
    calc.delete(0, END)
    calc.insert(0, a + b)

def znak(z):
    a = calc.get()
    if a[-1] in '-+/*':
        a = a[:-1]
    elif '+' in a or '-' in a or'*' in a or'/' in a:
        calculate()
        a = calc.get()
    calc.delete(0, END)
    calc.insert(0, a + z)

def itog():
    a = calc.get()
    if a[-1] in '-+/*':
        a = a+a[:-1]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(a))
    except (NameError, SyntaxError):
        messagebox.showinfo('calc', 'вводите только числа')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('calc', 'на ноль делить нельзя')
        calc.insert(0, 0)

def kvadr():
    a = calc.get()
    a = float(a)
    a = a**2
    calc.delete(0, END)
    calc.insert(0, a)
    
def prot():
    a = calc.get()
    a = float(a)
    a = a*(-1)
    calc.delete(0, END)
    calc.insert(0, a)
    
def chist():
    calc.delete(0, END)
    calc.insert(0, 0)
    
def itogknop(z):
    return Button(text=z, font=15,
                     command=itog)

def chistka(z):
    return Button(text=z, font=15,
                     command=chist)

def znakiknop(z):
    return Button(text=z,  font=15,
                     command=lambda : znak(z))

def kvadrknop(z):
    return Button(text=z,  font=15,
                     command=kvadr)

def protivopknop(z):
    return Button(text=z,  font=15,
                     command=prot)

def chisl(b):
    return Button(text=b,  font=15,
                     command=lambda : summ(b))

tk=Tk()
tk.geometry('240x360')

tk.title("Calc")

calc = Entry(tk, justify=RIGHT, font=15)
calc.insert(0, '0')
calc.place(x=15, y=20, width=220, height=30)

chisl('1').place(x=0, y=250, width=60, height=60)
chisl('2').place(x=60, y=250, width=60, height=60)
chisl('3').place(x=120, y=250, width=60, height=60)
chisl('4').place(x=0, y=190, width=60, height=60)
chisl('5').place(x=60, y=190, width=60, height=60)
chisl('6').place(x=120, y=190, width=60, height=60)
chisl('7').place(x=0, y=130, width=60, height=60)
chisl('8').place(x=60, y=130, width=60, height=60)
chisl('9').place(x=120, y=130, width=60, height=60)
chisl('0').place(x=60, y=310, width=60, height=60)
chisl('.').place(x=120, y=310, width=60, height=60)


znakiknop('+').place(x=180, y=310, width=60, height=60)
znakiknop('-').place(x=180, y=250, width=60, height=60)
znakiknop('*').place(x=180, y=190, width=60, height=60)
znakiknop('/').place(x=180, y=130, width=60, height=60)

kvadrknop('^2').place(x=60, y=70, width=60, height=60)
protivopknop('+/-').place(x=120, y=70, width=60, height=60)
chistka('c').place(x=0, y=70, width=60, height=60)
itogknop('=').place(x=180, y=70, width=60, height=60)

tk.mainloop()