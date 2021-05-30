
from tkinter import *
raiz=Tk()
raiz.title("Calculadora")


frame1=Frame(raiz,width="300",height="450")
frame1.pack()

#---------------pantalla--------------------
numeroPantalla=StringVar()

pantalla=Entry(frame1,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(bg="grey",fg="#03f943",justify="right")

#---------------Variables-------------------
reset_pantalla=True
operacion=""
resultado=0
num1=0
contador_resta=0
contador_mult=0
contador_div=0
#---------------Pulsaciones teclado----------
def numeroPulsado(num):
	global operacion
	global reset_pantalla
	
	if numeroPantalla.get()=="0":
		numeroPantalla.set("")

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False
	else:	
		numeroPantalla.set(numeroPantalla.get() + num)


#---------------Borrar pantalla--------------------
def borrar_pantalla():
	global operacion
	global resultado
	global num1, contador_resta,contador_mult,contador_div
	contador_resta=0
	contador_mult=0
	contador_div=0
	numeroPantalla.set("")
	operacion=""
	resultado=0
	num1

def volver(num):
	numeroPantalla.set(num[0:len(num)-1])
#---------------Funcion suma-----------------------

def suma(num):
	global operacion
	global resultado
	global reset_pantalla
	resultado+=int(num)
	operacion="suma"
	reset_pantalla=True
	numeroPantalla.set(resultado)
#---------------Funcion resta-----------------------

def resta(num):
	global operacion
	global resultado
	global reset_pantalla
	global num1
	global contador_resta

	if contador_resta==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-int(num)
		else:
			resultado=int(resultado)-int(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_resta+=1
	reset_pantalla=True
	operacion="resta"

#---------------Funcion Multiplicacion------------

def Mult(num):
	global operacion
	global resultado
	global contador_mult
	global reset_pantalla
	global num1
	if contador_mult==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_mult==1:
			resultado=num1*int(num)
		else:
			resultado=int(resultado)*int(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_mult+=1
	operacion="multiplicacion"
	reset_pantalla=True
			
#---------------Funcion Division-----------------

def Div(num):
	global operacion
	global resultado
	global contador_div
	global reset_pantalla
	global num1
	if contador_div==0:
		num1=int(num)
		resultado=float(num1)
	else:
		if contador_div==1:
			resultado=num1/int(num)
		else:
			resultado=int(resultado)/int(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_div=contador_div+1
	operacion="division"
	reset_pantalla=True
			
#---------------Funcion el_resultado------------

def el_resultado():
	global resultado
	global operacion

	if operacion=="suma":
		numeroPantalla.set(int(resultado)+int(numeroPantalla.get()))
		resultado=0
	elif operacion=="resta":
		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
		resultado=0
		contador_resta=0
	elif operacion=="division":
		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
		resultado=0
		contador_div=0
	elif operacion=="multiplicacion":
		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
		resultado=0
		contador_mult=0

#---------------Fila 0-----------------------
botonBorrar=Button(frame1,text="CE",width=8,command=lambda:borrar_pantalla())
botonBorrar.grid(row=2,column=1,columnspan=2)
botonVolver=Button(frame1,text="C",width=2,command=lambda:volver(numeroPantalla.get()))
botonVolver.grid(row=2,column=3,columnspan=1)



#---------------Fila 1-----------------------

boton7=Button(frame1,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=3,column=1)
boton8=Button(frame1,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2)
boton9=Button(frame1,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=3,column=3)
botonDiv=Button(frame1,text="/",width=3,command=lambda:Div(numeroPantalla.get()))
botonDiv.grid(row=3,column=4)

#---------------Fila 2-----------------------

boton4=Button(frame1,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=4,column=1)
boton5=Button(frame1,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2)
boton6=Button(frame1,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3)
botonMult=Button(frame1,text="X",width=3,command=lambda:Mult(numeroPantalla.get()))
botonMult.grid(row=4,column=4)

#---------------Fila 3-----------------------

boton1=Button(frame1,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=5,column=1)
boton2=Button(frame1,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2)
boton3=Button(frame1,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3)
botonRest=Button(frame1,text="-",width=3,command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=5,column=4)

#---------------Fila 4-----------------------

boton0=Button(frame1,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=6,column=2)
botonComa=Button(frame1,text=",",width=3,command=lambda:numeroPulsado(","))
botonComa.grid(row=6,column=1)
botonIgual=Button(frame1,text="=",width=3,command=lambda:el_resultado())
botonIgual.grid(row=6,column=3)
botonSuma=Button(frame1,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=6,column=4)






raiz.mainloop()