import sqlite3
from tkinter import *
import tkinter as tk

# VENTANA PRINCIPAL     
ventana1=Tk()
ventana1.title("VENTANA PRINCIPAL")
ventana1.resizable(False, True)
ventana1.geometry("1200x1050")
ventana1.config(bg="Sky blue")
label = Label(ventana1, text="Sistema de inventario tienda Pepito.", font=25)
label.place(x=350, y=20)
#Etiquetas de texto y entras del precio del producto 
label = Label(ventana1, text="Ingresa el nombre del producto.", bg="Sky blue", font=15)
label.place(x=250, y=70)
nombre = Entry(ventana1)
nombre.place(x=490, y=70, height=30, width=250)
#precio
label = Label(ventana1, text="Ingresa el precio del producto.", bg="Sky blue", font=15)
label.place(x=250, y=110)
precio = Entry(ventana1)
precio.place(x=490, y=110, height=30, width=250)
#ingresados
texto_datos = Text(ventana1, width=40, height=10)
texto_datos.place(x=150, y=280, height=700, width=900)
#mostrar datos en app
def mostrar_datos():
    cursorBD.execute('''SELECT * FROM PRODUCTO ORDER BY NOMBRE''')
    lista = cursorBD.fetchall()
    texto_datos.delete(1.0, END)  # Limpiar el área de texto
    for fila in lista:
        texto_datos.insert(END, f"Nombre: {fila[1]}, Precio: {fila[2]}\n")

# Botón para mostrar los datos
boton_mostrar = Button(ventana1, text="Mostrar datos", command=mostrar_datos)
boton_mostrar.place(x=400, y=220, height=30, width=100)

#botones
def insertarProducto():
    try:
        nombre_producto = nombre.get()
        if nombre_producto == "":
            print("Error: El nombre del producto no puede estar vacío")
            return
        precio_producto = float(precio.get())
        cursorBD.execute('''INSERT INTO PRODUCTO (NOMBRE, PRECIO) VALUES (?,?) ''', (nombre_producto, precio_producto))
        conexion.commit()
        print("Producto agregado correctamente")
    except ValueError:
        print("Error: El precio debe ser un número")

boton = Button(ventana1, text="Agregar Producto", command=insertarProducto)
boton.place(x=400, y=180, height=30, width=200)



conexion = sqlite3.connect('BaseDeDatos')
cursorBD = conexion.cursor()

def tablaExiste(nombreTabla):
    cursorBD.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombreTabla))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE PRODUCTO (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIO REAL) ''')
        return False

tablaExiste('PRODUCTO')

def seleccionarProductos():
    cursorBD.execute(''' SELECT * FROM PRODUCTO''')
    lista=[ ]
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

print(seleccionarProductos())


ventana1.mainloop()