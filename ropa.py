import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter.font import Font

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("ROPA")
        #tamaño ventanas
        
        self.ventana1.geometry("800x800")
        self.canvas1=tk.Canvas()

        self.ventana1 ['bg'] = 'maroon'
        
        bigFont=Font(family="Trebuchet",size=27, weight="bold", slant="roman", underline=0, overstrike=0)
        mediumFont= Font(family="Trebuchet",size=15, weight="normal", slant="roman", underline=0, overstrike=0)


       
        #estructura de inicio de sesion

        self.label1=tk.Label(self.ventana1,text="J.A.H", font=bigFont)
        self.label1.grid(column=2, row=1, padx=100, pady=100, sticky="n")

        self.label1=tk.Label(self.ventana1,text="Ingrese nombre de usuario:", font=mediumFont)
        self.label1.grid(column=2, row=1, padx=300, pady=210, sticky="n")

        #nombre de usuario
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, textvariable=self.dato)
        self.entry1.grid(column=2, row=1, pady=240, sticky="n")
        #boton de ingreso
        self.boton1=tk.Button(self.ventana1, text="Ingresar",font=mediumFont, command=self.ingresar)
        self.boton1.grid(column=2, row=1, pady=400, sticky="n")
        #contraseña
        self.dato1=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, textvariable=self.dato1)
        self.entry2.grid(column=2, row=1, pady=350, sticky="n")
        self.label2=tk.Label(self.ventana1,text="Ingrese su contraseña:",font=mediumFont)
        self.label2.grid(column=2, row=1, padx=300, pady=320, sticky="n")
        self.ventana1.mainloop()

    def ingresar(self):
        self.ventana1.destroy
        self.ventana1.withdraw()
        self.ventana2=tk.Toplevel()
        
        self.ventana2.title("ROPA")
        self.ventana2.geometry("800x800")
        self.ventana2 ['bg'] = 'firebrick4'

        mediumFont= Font(family="Trebuchet",size=15, weight="normal", slant="roman", underline=0, overstrike=0)

        self.label3=tk.Label(self.ventana2, text="Seleccione las prendas que desea comprar B)", font=mediumFont)
        self.label3.grid(column=2, row=1, padx=200, pady=100, sticky="n")
        self.scroll1 =tk.Scrollbar(self.ventana2, orient=VERTICAL)
        self.listbox1=tk.Listbox(self.ventana2, selectmode=MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=2, row=1, pady=250, sticky="n")
         
        self.listbox1.insert(0,"Remeras")
        self.listbox1.insert(1,"Buzos")
        self.listbox1.insert(2,"Pantalones")
        self.listbox1.insert(3,"Zapatillas")
        self.listbox1.insert(4,"Camperas")
       
        self.boton3=tk.Button(self.ventana2, text="Siguiente", command=self.siguiente, font=mediumFont)
        self.boton3.grid(column=2, row=1, pady=500, sticky="n")

       # self.ventana2.mainloop()

    def siguiente(self):
        self.ventana2.destroy
        self.ventana2.withdraw()
        self.ventana3=tk.Toplevel()

        self.ventana3.title("ROPA")
        self.ventana3.geometry("800x800")

        mediumFont= Font(family="Trebuchet",size=15, weight="normal", slant="roman", underline=0, overstrike=0)
    
        self.ventana3 ['bg'] = 'maroon'
        
        self.img1=tk.PhotoImage(file="neg.png")
        self.labelimagen1=tk.Label(self.ventana3, image=self.img1).place(x=40, y=60)

        self.img2=tk.PhotoImage(file="ful.png")
        self.labelimagen2=tk.Label(self.ventana3, image=self.img2).place(x=30, y=250)

        self.img3=tk.PhotoImage(file="oso.png")
        self.labelimagen3=tk.Label(self.ventana3, image=self.img3).place(x=30, y=500)


        #botones
        self.boton4=tk.Button(self.ventana3, text="Comprar",font=mediumFont)
        self.boton4.place(x=300,y=130)

        self.boton5=tk.Button(self.ventana3, text="Comprar",font=mediumFont)
        self.boton5.place(x=300,y=350)

        self.boton5=tk.Button(self.ventana3, text="Comprar",font=mediumFont)
        self.boton5.place(x=300,y=550)

        #self.ventana3.mainloop()

aplicacion1=Aplicacion()

