import tkinter as ven
from tkinter import ttk
from vpython import *
primordial=[]
temp=[]
def graficar():
	caja=box(pos=vector(temp[0],temp[1],temp[2]),size=vector(1,1,1),color=color.green)
def segunda():
	for i in primordial:
		i.split(",")
		temp.append(int(i[0]))
		temp.append(int(i[2]))
		temp.append(int(i[4]))
	segunda=ven.Toplevel()
	segunda.config(width=300,height=300)
	segunda.title("segunda")
	iniciar=ven.Label(segunda,text="se ingresearan las siguentes coordenadas: ")
	iniciar.place(x=10,y=50)
	mostrar=ven.Label(segunda,text=temp)
	mostrar.place(x=10,y=100)
	iniciargrafica=ven.Button(segunda,text="iniciar",command=lambda: graficar())
	iniciargrafica.place(x=10,y=150)
def principal():
	root=ven.Tk()
	root.config(width=400,height=400)
	root.title("prueba")
	entrada=ven.Label(text="ingrese coordenadas en el modo (x,y,z)")
	entrada.place(x=10,y=10)
	entrada=ven.Entry(root)
	entrada.place(x=10,y=50)
	anexarlista=ven.Button(root,text="ingresar coordenadas",
	command=lambda: primordial.append(entrada.get()))
	anexarlista.place(x=10,y=90)
	mostrarlista=ven.Button(root,text="mostrar",command=lambda: segunda())
	mostrarlista.place(x=10,y=120)
	root.mainloop()
principal()
