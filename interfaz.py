from tkinter import *  

### Funciones ###

# Ventanas secundarias 
def ventana_secundaria(raiz, title):
    nueva_ventana = Toplevel(raiz)
    nueva_ventana.title(title)
    nueva_ventana.config(width=500, height=500)
  
    return nueva_ventana
    
# Se crea ventana principal, titulo y tamaño

ventana_principal = Tk()
ventana_principal.title("Negocio 2024")
ventana_principal.config(width=500, height=500)

# Ventanas secundarias 

ventana_clientes = ventana_secundaria(ventana_principal, 'Clientes')
ventana_stocks = ventana_secundaria(ventana_principal, 'Stocks')
ventana_pedidos = ventana_secundaria(ventana_principal, 'Pedidos')
ventana_ventas = ventana_secundaria(ventana_principal, 'Ventas')

# Labels (etiquetas de texto)

label = Label(ventana_principal, 'Texto')

# Botones

clientes = Button(ventana_principal, text= 'Clientes', command= ventana_clientes)
stocks = Button(ventana_principal, text= 'Stocks', command= ventana_stocks)
pedidos = Button(ventana_principal, text= 'Pedidos', command= ventana_pedidos)
ventas = Button(ventana_principal, text= 'Ventas', command= ventana_ventas)






ventana_principal.mainloop()
