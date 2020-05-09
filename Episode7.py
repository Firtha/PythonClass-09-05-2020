# Il manque la mise a jour des valeurs via le clic du bouton CLEAN, a retravailler si le temps est suffisant

from tkinter import *

def updateValues():
    print("test clic value",value)


fenetre = Tk()

Label(fenetre, text="Source :").pack()

value = StringVar()
value.set("\\B\\T80CM\\T60CM\\N")
Entry(fenetre, textvariable=value, width=30).pack()

Button(fenetre, text="Clean", command=updateValues).pack()

Label(fenetre, text="Destination").pack()

value1 = StringVar()
value1.set("80CM")
Entry(fenetre, textvariable=value1, width=10).pack(side=LEFT, padx=15)

value2 = StringVar()
value2.set("60CM")
Entry(fenetre, textvariable=value2, width=10).pack(side=RIGHT, padx=15)

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Fermer', command=fenetre.quit).pack(side=LEFT, padx=125, pady=5)

fenetre.mainloop()