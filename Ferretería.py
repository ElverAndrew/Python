from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from sys import *

def Informacion():

    #Una tabla de información con los códigos y precios de los productos  
         
    root = Tk() 
    root.geometry("900x670")
    root.title('Información de productos')
    root.config(bg= "#5DC1B9")
    root.resizable(False,False)

    miFrame = Frame(root)
    miFrame.pack() 
    miFrame.config(bg = "#5DC1B9")
    lDni = Label(miFrame, text='Códigos de producto', font=("calibri", 50),bg= "#5DC1B9" )
    lDni.grid(row=0, column=3, pady=15, padx=15)
  
    arbol= ttk.Treeview(root,height=25,columns=("Producto", "Precio"))
    arbol.heading("#0", text="Código")
    arbol.heading("Producto", text="Producto")
    arbol.heading("Precio", text="Precio")
    arbol.insert("",1, text=1, values=("Tornillo",0.50))
    arbol.insert("",2, text=2, values=("Clavo", 0.50))
    arbol.insert("",3, text=3, values=("Engrapadora", 90.0))
    arbol.insert("",4, text=4, values=("Martillo", 15.0))
    arbol.insert("",5, text=5, values=("Taladro", 180.0))
    arbol.insert("",6, text=6, values=("Escuadra", 25.0))
    arbol.insert("",7, text=7, values=("Remachadora", 40.0))
    arbol.insert("",8, text=8, values=("Remache", 0.20))
    arbol.insert("",9, text=9, values=("Sierra", 35.0))
    arbol.insert("",10, text=10, values=("Alicate", 18.0))
    arbol.insert("",11, text=11, values=("Desarmador", 8.0))
    arbol.insert("",12, text=12, values=("Moladora", 220.0))
    arbol.insert("",13, text=13, values=("Dados", 2.50))
    arbol.insert("",14, text=14, values=("Cemento", 40.0))
    arbol.insert("",15, text=15, values=("Pintura", 23.0))
    arbol.insert("",16, text=16, values=("Cerradura", 80.0))
    arbol.insert("",17, text=17, values=("Varilla", 25.0))
    arbol.insert("",18, text=18, values=("Triplay", 30.0))
    arbol.insert("",19, text=19, values=("Madera", 5.0))
    arbol.insert("",20, text=20, values=("Listón", 18.0))
    arbol.insert("",21, text=21, values=("Puerta", 150.0))
    arbol.insert("",22, text=22, values=("Bisagra", 3.0))
    arbol.insert("",23, text=23, values=("Yeso", 4.0))
    arbol.insert("",24, text=24, values=("Silicona", 6.0))
    arbol.insert("",END, text=25, values=("Nivelador", 15.0))
    
    arbol.place(x=150,y=130)

def Extra():
    root = Tk() 
    root.geometry("700x350")
    root.title('Información adicional')
    root.config(bg= "#5DC1B9")
    root.resizable(False,False)

    miFrame = Frame(root)
    miFrame.pack() 
    miFrame.config(bg = "#5DC1B9")
    lDni = Label(miFrame, text='Programa creado por Elver Andrew Quevedo Valer', font=("calibri", 20),bg= "#5DC1B9" )
    lDni.grid(row=0, column=3, pady=15, padx=15)

    lDni1 = Label(miFrame, text='09/09/2021', font=("calibri", 20),bg= "#5DC1B9" )
    lDni1.grid(row=2, column=3, pady=15, padx=15)

    lDni2 = Label(miFrame, text='Proyecto de Algoritmia de Programación del Software', font=("calibri", 20),bg= "#5DC1B9" )
    lDni2.grid(row=3, column=3, pady=15, padx=15)

    lDni3 = Label(miFrame, text='Instituto Superior Tecnológico SENATI', font=("calibri", 20),bg= "#5DC1B9" )
    lDni3.grid(row=4, column=3, pady=15, padx=15)

    lDni4 = Label(miFrame, text='Estudiante de Ingeniería de Software con Inteligencia Artificial', font=("calibri", 20),bg= "#5DC1B9" )
    lDni4.grid(row=5, column=3, pady=15, padx=15)

 
def Calculo():

    #Calcula el subtotal y el total a pagar

    try:

        cant=int(obtenerCantidad.get());
        cant1=int(obtenerCantidad1.get());
        cant2=int(obtenerCantidad2.get());
        prec=float(obtenerPrecio.get());
        prec1=float(obtenerPrecio1.get());
        prec2=float(obtenerPrecio2.get());
       
        subt=(cant*prec);
        subt1=(cant1*prec1);
        subt2=(cant2*prec2);

        totl = (subt+subt1+subt2);
   
        obtenerSubtotal.set(str(subt));
        obtenerSubtotal1.set(str(subt1));
        obtenerSubtotal2.set(str(subt2));
 
        obtenerTotal.set(str(totl));
        

    except ValueError:
            MessageBox.showinfo("AVISO IMPORTANTE","""Por favor rellene la columna de Cantidad.
Ingrese solo numeros y evite dejar celdas vacias.


                        *********************
                        | Mensaje de ayuda |
                        *********************
Puede ingresar solo los codigos de productos y el sistema te arrojará los precios presionando Completar""");

    
def Codigos():
    
    try:
        codg=int(obtenerCodigo.get());
        codg1=int(obtenerCodigo1.get());
        codg2=int(obtenerCodigo2.get());
        prod=obtenerProducto.get();
        prod1=obtenerProducto1.get();
        prod2=obtenerProducto2.get();
        prec=obtenerPrecio.get();
        prec1=obtenerPrecio1.get();
        prec2=obtenerPrecio2.get();


        uni=obtenerUnidad.get();
        uni1=obtenerUnidad1.get();
        uni2=obtenerUnidad2.get();

        #Condición por código para los productos de la primera columna
        if codg == 1:
            prod = "Tornillo   "
            prec= 0.50
            uni = "Unidad"
        elif codg == 2:
            prod = "Clavo      "
            prec= 0.50
            uni= "Unidad"
        elif codg == 3:
            prod = "Engrapadora"
            prec= 90
            uni= "Unidad"
        elif codg == 4:
            prod = "Martillo   "
            prec= 15
            uni= "Unidad"
        elif codg == 5:
            prod = "Taladro    "
            prec= 180
            uni= "Unidad"
        elif codg == 6:
            prod = "Escuadra   "
            prec= 25
            uni= "Unidad"
        elif codg == 7:
            prod = "Remachadora"
            prec= 40
            uni= "Unidad"
        elif codg == 8:
            prod = "Remache    "
            prec= 0.20
            uni= "Unidad"
        elif codg == 9:
            prod = "Sierra     "
            prec= 35
            uni= "Unidad"
        elif codg == 10:
            prod = "Alicate    "
            prec= 18
            uni= "Unidad"
        elif codg == 11:
            prod = "Desarmador "
            prec= 8
            uni= "Unidad"
        elif codg == 12:
            prod = "Moladora   "
            prec= 220
            uni= "Unidad"
        elif codg == 13:
            prod = "Dados      "
            prec= 2.50
            uni= "Unidad"
        elif codg == 14:
            prod = "Cemento    "
            prec= 40
            uni= "Unidad"
        elif codg == 15:
            prod = "Pintura    "
            prec= 23
            uni= "Unidad"
        elif codg == 16:
            prod = "Cerradura  "
            prec= 80
            uni= "Unidad"
        elif codg == 17:
            prod = "Varilla    "
            prec= 25
            uni= "Unidad"
        elif codg == 18:
            prod = "Triplay    "
            prec= 30
            uni= "Unidad"
        elif codg == 19:
            prod = "Madera     "
            prec= 5
            uni= "Unidad"
        elif codg == 20:
            prod = "Listón     "
            prec= 18
            uni= "Unidad"
        elif codg == 21:
            prod = "Puerta     "
            prec= 150
            uni= "Unidad"
        elif codg == 22:
            prod = "Bisagra    "
            prec= 3
            uni= "Unidad"
        elif codg == 23:
            prod = "Yeso       "
            prec= 4
            uni= "Unidad"
        elif codg == 24:
            prod = "Silicona   "
            prec= 6
            uni= "Unidad"
        elif codg == 25:
            prod = "Nivelador  "
            prec= 15
            uni= "Unidad"
        
        else:
            a=None

        #Condición por código para los productos de la segunda columna
        if codg1 == 1:
            prod1 = "Tornillo   "
            prec1= 0.50
            uni1 = "Unidad"
        elif codg1 == 2:
            prod1 = "Clavo      "
            prec1= 0.50
            uni1= "Unidad"
        elif codg1 == 3:
            prod1 = "Engrapadora"
            prec1= 90
            uni1= "Unidad"
        elif codg1 == 4:
            prod1 = "Martillo   "
            prec1= 15
            uni1= "Unidad"
        elif codg1 == 5:
            prod1 = "Taladro    "
            prec1= 180
            uni1= "Unidad"
        elif codg1 == 6:
            prod1 = "Escuadra   "
            prec1= 25
            uni1= "Unidad"
        elif codg1 == 7:
            prod1 = "Remachadora"
            prec1= 40
            uni1= "Unidad"
        elif codg1 == 8:
            prod1 = "Remache    "
            prec1= 0.20
            uni1= "Unidad"
        elif codg1 == 9:
            prod1 = "Sierra     "
            prec1= 35
            uni1= "Unidad"
        elif codg1 == 10:
            prod1 = "Alicate    "
            prec1= 18
            uni1= "Unidad"
        elif codg1 == 11:
            prod1 = "Desarmador "
            prec1= 8
            uni1= "Unidad"
        elif codg1 == 12:
            prod1 = "Moladora   "
            prec1= 220
            uni1= "Unidad"
        elif codg1 == 13:
            prod1 = "Dados      "
            prec1= 2.50
            uni1= "Unidad"
        elif codg1 == 14:
            prod1 = "Cemento    "
            prec1= 40
            uni1= "Unidad"
        elif codg1 == 15:
            prod1 = "Pintura    "
            prec1= 23
            uni1= "Unidad"
        elif codg1 == 16:
            prod1 = "Cerradura  "
            prec1= 80
            uni1= "Unidad"
        elif codg1 == 17:
            prod1 = "Varilla    "
            prec1= 25
            uni1= "Unidad"
        elif codg1 == 18:
            prod1 = "Triplay    "
            prec1= 30
            uni1= "Unidad"
        elif codg1 == 19:
            prod1 = "Madera     "
            prec1= 5
            uni1= "Unidad"
        elif codg1 == 20:
            prod1 = "Listón     "
            prec1= 18
            uni1= "Unidad"
        elif codg1 == 21:
            prod1 = "Puerta     "
            prec1= 150
            uni1= "Unidad"
        elif codg1 == 22:
            prod1 = "Bisagra    "
            prec1= 3
            uni1= "Unidad"
        elif codg1 == 23:
            prod1 = "Yeso       "
            prec1= 4
            uni1= "Unidad"
        elif codg1 == 24:
            prod1 = "Silicona   "
            prec1= 6
            uni1= "Unidad"
        elif codg1 == 25:
            prod1 = "Nivelador  "
            prec1= 15
            uni1= "Unidad"
        
        else:
            a=None

        #Condición por código para los productos de la tercera columna
        if codg2 == 1:
            prod2 = "Tornillo   "
            prec2= 0.50
            uni2 = "Unidad"
        elif codg2 == 2:
            prod2 = "Clavo      "
            prec2= 0.50
            uni2= "Unidad"
        elif codg2 == 3:
            prod2 = "Engrapadora"
            prec2= 90
            uni2= "Unidad"
        elif codg2 == 4:
            prod2 = "Martillo   "
            prec2= 15
            uni2= "Unidad"
        elif codg2 == 5:
            prod2 = "Taladro    "
            prec2= 180
            uni2= "Unidad"
        elif codg2 == 6:
            prod2 = "Escuadra   "
            prec2= 25
            uni2= "Unidad"
        elif codg2 == 7:
            prod2 = "Remachadora"
            prec2= 40
            uni2= "Unidad"
        elif codg2 == 8:
            prod2 = "Remache    "
            prec2= 0.20
            uni2= "Unidad"
        elif codg2 == 9:
            prod2 = "Sierra     "
            prec2= 35
            uni2= "Unidad"
        elif codg2 == 10:
            prod2 = "Alicate    "
            prec2= 18
            uni2= "Unidad"
        elif codg2 == 11:
            prod2 = "Desarmador "
            prec2= 8
            uni2= "Unidad"
        elif codg2 == 12:
            prod2 = "Moladora   "
            prec2= 220
            uni2= "Unidad"
        elif codg2 == 13:
            prod2 = "Dados      "
            prec2= 2.50
            uni2= "Unidad"
        elif codg2 == 14:
            prod2 = "Cemento    "
            prec2= 40
            uni2= "Unidad"
        elif codg2 == 15:
            prod2 = "Pintura    "
            prec2= 23
            uni2= "Unidad"
        elif codg2 == 16:
            prod2 = "Cerradura  "
            prec2= 80
            uni2= "Unidad"
        elif codg2 == 17:
            prod2 = "Varilla    "
            prec2= 25
            uni2= "Unidad"
        elif codg2 == 18:
            prod2 = "Triplay    "
            prec2= 30
            uni2= "Unidad"
        elif codg2 == 19:
            prod2 = "Madera     "
            prec2= 5
            uni2= "Unidad"
        elif codg2 == 20:
            prod2 = "Listón     "
            prec2= 18
            uni2= "Unidad"
        elif codg2 == 21:
            prod2 = "Puerta     "
            prec2= 150
            uni2= "Unidad"
        elif codg2 == 22:
            prod2 = "Bisagra    "
            prec2= 3
            uni2= "Unidad"
        elif codg2 == 23:
            prod2 = "Yeso       "
            prec2= 4
            uni2= "Unidad"
        elif codg2 == 24:
            prod2 = "Silicona   "
            prec2= 6
            uni2= "Unidad"
        elif codg2 == 25:
            prod2 = "Nivelador  "
            prec2= 15
            uni2= "Unidad"
        
        else:
            a=None
        
        obtenerCodigo.set(str(codg));
        obtenerCodigo1.set(str(codg1));
        obtenerCodigo2.set(str(codg2));

        obtenerProducto.set(str(prod));
        obtenerProducto1.set(str(prod1));
        obtenerProducto2.set(str(prod2))

        obtenerPrecio.set(float(prec));
        obtenerPrecio1.set(float(prec1));
        obtenerPrecio2.set(float(prec2));


        obtenerUnidad.set(str(uni));
        obtenerUnidad1.set(str(uni1));
        obtenerUnidad2.set(str(uni2));
    except ValueError:
            MessageBox.showinfo("AVISO IMPORTANTE","""En la columna Cod_Prod ingrese un numero válido.
Por favor evite dejar casillas vacias
    
NOTA: Los códigos de productos están en una nueva ventana en la parte superior izquierda.""");


def Limpiar():

    #Limpieza de las cajas de entrada de texto

    obtenerCodigo.set("");
    obtenerCodigo1.set("");
    obtenerCodigo2.set("");
    obtenerProducto.set("");
    obtenerProducto1.set("");
    obtenerProducto2.set("");
    obtenerUnidad.set("");
    obtenerUnidad1.set("");
    obtenerUnidad2.set("");
    obtenerCantidad.set("");
    obtenerCantidad1.set("");
    obtenerCantidad2.set("");
    obtenerPrecio.set("");
    obtenerPrecio1.set("");
    obtenerPrecio2.set("")
    obtenerSubtotal.set("");
    obtenerSubtotal1.set("");
    obtenerSubtotal2.set("");
    obtenerTotal.set("");
    obtenerDni.set("");
    obtenerApellido.set("");
    obtenerNombre.set("");
    obtenerDir.set("");
    obtenerTel.set("");
    
#VENTANA PRINCIPAL

root = Tk() 
root.title('') 
root.config(bg= "#5DC1B9")

root.resizable(False,False)

miFrame = Frame(root)
miFrame.pack()
miFrame.config(bg= "#5DC1B9")


lDni = Label(miFrame, text='Ferretería El Tornillo Feliz', font=("monotype corsiva", 20), bg = "#5DC1B9", fg = "black")
lDni.grid(row=0, column=2, pady=10, padx=10)

#DNI --------------------------------
obtenerDni=StringVar() 
lDni = Label(miFrame, text='DNI:', bg = "#5DC1B9")
lDni.grid(row=5, column=0, sticky='e', pady=5, padx=5)
tDni = Entry(miFrame,textvariable=obtenerDni)
tDni.grid(row=5, column=1, pady=5, padx=5)

#Apellido --------------------------------
obtenerApellido=StringVar() 
lApellido = Label(miFrame, text='Apellido:', bg = "#5DC1B9")
lApellido.grid(row=6, column=0, sticky='e', pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=6, column=1, pady=5, padx=5)
#Nombre --------------------------------
obtenerNombre=StringVar()
lNombre = Label(miFrame, text='Nombre:', bg = "#5DC1B9")
lNombre.grid(row=6, column=2, sticky='e', pady=5, padx=5)
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=6, column=3, pady=5, padx=5)
#Dirección --------------------------------
obtenerDir=StringVar() 
lDireccion = Label(miFrame, text='Dirección:', bg = "#5DC1B9")
lDireccion.grid(row=7, column=0, sticky='e', pady=5, padx=5)
tDireccion = Entry(miFrame,textvariable=obtenerDir)
tDireccion.grid(row=7, column=1, columnspan=3, sticky='we',pady=5, padx=5)
#Teléfono --------------------------------
obtenerTel=StringVar() 
lTel = Label(miFrame, text='Teléfono:', bg= "#5DC1B9")
lTel.grid(row=8, column=0, sticky='e', pady=5, padx=5)
tTel = Entry(miFrame,textvariable=obtenerTel)
tTel.grid(row=8, column=1,columnspan=3, sticky='we', pady=5, padx=5)

miFrame1 = Frame(root)
miFrame1.pack()
miFrame1.config(bg = "#5DC1B9")



#Variables (CÓDIGO)
obtenerCodigo = StringVar()
obtenerCodigo1 = StringVar()
obtenerCodigo2 = StringVar()

lCodigo = Label(miFrame1, text='Cod_Prod', bg= "#5DC1B9")
lCodigo.grid(row=9, column=0,sticky='e', pady=5, padx=5)
tCodigo1 = Entry(miFrame1, width=7, textvariable =obtenerCodigo)
tCodigo1.grid(row=10, column=0, pady=5, padx=5)
tCodigo2 = Entry(miFrame1, width=7,textvariable =obtenerCodigo1)
tCodigo2.grid(row=11, column=0, pady=5, padx=5)
tCodigo3 = Entry(miFrame1, width=7,textvariable =obtenerCodigo2)
tCodigo3.grid(row=12, column=0, pady=5, padx=5)


#variables (PRODUCTO)
obtenerProducto = StringVar() 
obtenerProducto1 =StringVar()
obtenerProducto2 =StringVar()

lDes = Label(miFrame1, text='Descripción', bg= "#5DC1B9")
lDes.grid(row=9, column=1,sticky='ew', pady=5, padx=5)
tDes1 = Entry(miFrame1, width=11, state="readonly",textvariable = obtenerProducto)
tDes1.grid(row=10, column=1, pady=5, padx=5)
tDes2 = Entry(miFrame1, width=11, state="readonly",textvariable = obtenerProducto1)
tDes2.grid(row=11, column=1, pady=5, padx=5)
tDes3 = Entry(miFrame1, width=11, state="readonly",textvariable = obtenerProducto2)
tDes3.grid(row=12, column=1, pady=5, padx=5)

#variableS (UNIDAD)
obtenerUnidad = StringVar() 
obtenerUnidad1 = StringVar()
obtenerUnidad2 = StringVar()

lUni = Label(miFrame1, text='Unidad', bg= "#5DC1B9")
lUni.grid(row=9, column=2,sticky='ew', pady=5, padx=5)
tUni1 = Entry(miFrame1, width=7, state="readonly", textvariable = obtenerUnidad)
tUni1.grid(row=10, column=2, pady=5, padx=5)
tUni2 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerUnidad1 )
tUni2.grid(row=11, column=2, pady=5, padx=5)
tUni3 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerUnidad2)
tUni3.grid(row=12, column=2, pady=5, padx=5)

#Variables (CANTIDAD)
obtenerCantidad = StringVar()
obtenerCantidad1 = StringVar()
obtenerCantidad2 = StringVar()

lCantidad = Label(miFrame1, text='Cantidad', bg = "#5DC1B9")
lCantidad.grid(row=9, column=3,sticky='ew', pady=5, padx=5)
tCantidad1 = Entry(miFrame1, width=7, textvariable = obtenerCantidad)
tCantidad1.grid(row=10, column=3, pady=5, padx=5)
tCantidad2 = Entry(miFrame1, width=7, textvariable = obtenerCantidad1)
tCantidad2.grid(row=11, column=3, pady=5, padx=5)
tCantidad3 = Entry(miFrame1, width=7, textvariable = obtenerCantidad2)
tCantidad3.grid(row=12, column=3, pady=5, padx=5)

#Variables (PRECIO)
obtenerPrecio = StringVar()
obtenerPrecio1 = StringVar()
obtenerPrecio2 = StringVar()

lPrecio = Label(miFrame1, text='Precio', bg = "#5DC1B9")
lPrecio.grid(row=9, column=4,sticky='ew', pady=5, padx=5)
tPrecio1 = Entry(miFrame1, width=7,state="readonly",textvariable = obtenerPrecio)
tPrecio1.grid(row=10, column=4, pady=5, padx=5)
tPrecio2 = Entry(miFrame1, width=7,state="readonly",textvariable = obtenerPrecio1)
tPrecio2.grid(row=11, column=4, pady=5, padx=5)
tPrecio3 = Entry(miFrame1, width=7,state="readonly",textvariable = obtenerPrecio2)
tPrecio3.grid(row=12, column=4, pady=5, padx=5)

#Variables (SUB TOTAL)
obtenerSubtotal = StringVar()
obtenerSubtotal1 = StringVar()
obtenerSubtotal2 = StringVar()

lSubtotal = Label(miFrame1, text='Subtotal', bg= "#5DC1B9")
lSubtotal.grid(row=9, column=5,sticky='ew', pady=5, padx=5)
tSubtotal1 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal)
tSubtotal1.grid(row=10, column=5, pady=5, padx=5)
tSubtotal2 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal1)
tSubtotal2.grid(row=11, column=5, pady=5, padx=5)
tSubtotal3 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal2)
tSubtotal3.grid(row=12, column=5, pady=5, padx=5)

#Variable (TOTAL)
obtenerTotal = StringVar() 
lTotal = Label(miFrame1, text='Total',font=("calibri", 12),bg= "#FFFF00")
lTotal.grid(row=12, column=6,sticky='ew', pady=5, padx=5)
tTotal = Entry(miFrame1, width=7, state="readonly", textvariable = obtenerTotal)
tTotal.grid(row=12, column=7, pady=5, padx=5)

def almacenar():

    #Almacena los datos ingresados

    MessageBox.showinfo("Mensaje de comprobacion", "Impresión completada")
    a = open('Comprobante.txt', 'w')
    a.write("Comprobante de Pago \n")
    a.write("\nFerretería El Tornillo Feliz\n")
    a.write("\nDNI:   " + tDni.get() + '\n' + "Apellido:   " + tApellido.get() +'\n' + "Nombre:   " + tNombre.get() + '\n' + "Dirección:   " + tDireccion.get() + '\n' + "Teléfono:   " + tTel.get())
    a.write("\n\nCod_Prod" + "  Descripción   " + "Unidad    "+ "Cantidad    " + "Precio    " + "Subtotal    ")
    a.write("\n" + "   "+tCodigo1.get()+"      "+ tDes1.get() + "   "+ tUni1.get() + "       "+ tCantidad1.get() + "         " +tPrecio1.get() +"       "+ tSubtotal1.get())
    a.write("\n" + "   "+tCodigo2.get()+"      "+ tDes2.get() + "   "+ tUni2.get() + "       "+ tCantidad2.get() + "         "+tPrecio2.get() + "       "+tSubtotal2.get())
    a.write("\n" + "   "+tCodigo3.get()+"      "+ tDes3.get() + "   "+ tUni3.get() + "       "+ tCantidad3.get() + "         "+tPrecio3.get() + "       "+tSubtotal3.get())
    a.write("\n" + "\nTotal a pagar:     " + tTotal.get() + " soles")
           
    a.close

#Botón Calcular
guardar=Button(miFrame1, text='Calcular',font=("calibri", 15),bg= "#FFFF00", command=Calculo)
guardar.grid(row=13, column=5, pady=10, padx=10)

#boton Completar
guardar=Button(miFrame1, text='Completar',font=("calibri", 12),bg= "#FFFF00", command=Codigos)
guardar.grid(row=13, column=1, pady=5, padx=5)

#boton Limpiar
guardar=Button(miFrame1, text='Limpiar', font=("calibri", 12),bg= "#FFFF00", command= Limpiar)
guardar.grid(row=13, column=0, pady=5, padx=5)

#boton Imprimir
guardar=Button(miFrame1, text='Imprimir', font=("calibri", 12),bg= "#FFFF00", command= almacenar)
guardar.grid(row=13, column=2, pady=5, padx=5)


Mi_Menu = Menu(root)
root.config(menu = Mi_Menu)
 
submenu = Menu(Mi_Menu, tearoff = 0)
Mi_Menu.add_cascade(label = "Información", menu = submenu)
 
submenu.add_command(label="Información de productos", command = Informacion)
submenu.add_command(label="Información adicional", command = Extra)
submenu.add_separator()
submenu.add_command(label="Salir", command = quit)

root.mainloop()