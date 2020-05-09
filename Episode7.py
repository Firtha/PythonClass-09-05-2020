# coding: utf-8

from tkinter import *
from tkinter.messagebox import *

def managePopup():
    if askyesno('Oups !', 'Il semblerait que ce bouton ne serve a rien !'):
        showwarning('Oui', 'Tant pis...')
    else:
        showinfo('Non', 'Et pourtant il semblerait que si...')
        showerror("Private Joke", "Même si c'est dommage :x")

def updateValues():
    str = input1.get()
    temp = re.findall(r'\d+', str)
    res = list(map(int, temp))
    input2.delete(0, END)
    input2.insert(0, res[0])
    input2.insert("end", "CM")
    input3.delete(0, END)
    input3.insert(0, res[1])
    input3.insert("end", "CM")


fenetre = Tk()

Label(fenetre, text="Source :").pack()

value = StringVar()
value.set("\\B\\T80CM\\T60CM\\N")
input1 = Entry(fenetre, textvariable=value, width=30)
input1.pack()

Button(fenetre, text="Clean", command=updateValues).pack()

Label(fenetre, text="Destination").pack()

value = StringVar()
value.set("80CM")
input2 = Entry(fenetre, textvariable=value, width=10)
input2.pack(side=LEFT, padx=15)

value = StringVar()
value.set("60CM")
input3 = Entry(fenetre, textvariable=value, width=10)
input3.pack(side=RIGHT, padx=15)

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Info', command=managePopup).pack(side=LEFT, padx=100, pady=5)
Button(fenetre, text ='Fermer', command=fenetre.quit).pack(side=LEFT, padx=150, pady=5)

fenetre.mainloop()