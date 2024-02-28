from tkinter import *
from tkinter import ttk


def mostrar(lista):
    seleccion = Listbox.curselection(lista)
    dato = Listbox.get(lista, seleccion[0])
    print(seleccion)
    print(dato)
    return seleccion


ventana = Tk()
ventana.config(width=300, height=300)

lista = Listbox(ventana, width=40, height=10, selectmode=BROWSE)
lista.place(x=10, y=50)
lista.insert(0, 'Probando')
lista.insert(1, 'Texto')
Button(ventana, text='Mostar', command=lambda: mostrar(lista)).place(x=70, y=20)


ventana.mainloop()
