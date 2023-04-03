"Bibliotecas Importadas"

import csv  # Formato del documento
import os  # Imagenes (direcciones de archivos)
import time  # Pondra la hora
from tkinter import *  # Interfaz
from tkinter import messagebox  # Interfaz
from tkinter import ttk  # tabla de datos
from PIL import Image, ImageTk  # Ajusta el tamaño de la imagen

"""
Globales
"""
productos = [] #lista de los productosf
movimientos = [] #lista de los movimientos
dinero = [] #lista del dinero disponible
transaccion = len(movimientos)  #Numero de transaccion

################################################
################################################

"""
Fondo: esta funcion resivira el nombre de una imagen para usarla
E: una iamgen
R: esta depende de del formato ya sea .png o .gif
S: retorna la imagen
"""
def Fondo(img):  
    ruta = os.path.join("Adicionales",img) 
    imagen = PhotoImage(file=ruta)
    return imagen

################################################

"""
Imagenes: esta funcion pondra imagenes con un tamaño determinado
E: una imagen
R: png o gif
S: la imagen con el tamaño indicado
"""
def Imagenes(img,size):
    ruta = None
    if size != None:
        ruta = Image.open("Adicionales/"+img).resize((size),Image.ANTIALIAS)
    else:
        ruta = Image.open("Adicionales/"+img)
    imagen = ImageTk.PhotoImage(ruta)
    return imagen

################################################

"""
correct: validad la contraseña
E: la contraseña
R: ninguna
S: la ventana administrador o cierra la ventana
"""
def correct(contraseña):
    if  "Computer" == contraseña:
        Administrador()
    else:
        Cerrar()

################################################    
"""
Cerrar: esta funcion cierra por completo el programa
"""
def Cerrar():
    ventana.destroy()
    
################################################
"""
reset: limpia la tabla de movimientos
E: la global de movimientos
R: que sea la tabla correcta
S: la tabla limpia
"""
def reset():
    movimientos = []
    LimpiarMovimientos()
    
################################################
"""
Funciones encargada de leer el archivo de productos, movimientos y dinero
Estas funciones simplemente leen los archivos, necesarios para el funcionamiento del programa
"""

"""
Productos: lee el archivo de productos que posee la maquina expendedorta
"""
def leerP():
    with open("Productos.csv",'r') as csvfile:
        csvreader = csv.reader(csvfile)  
        for line in csvreader:
            productos.append(line)
    
"""
Movimientos: registro de movimienyos de la maquina expendedora
"""            
def leerM():
    with open("Movimientos.csv",'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            movimientos.append(line)
    
"""
Dinero: registro de dinero disponible en la maquina expendedora
"""
def leerD():
    with open("Dinero.csv",'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            dinero.append(line)

################################################

"""
Estas funciones se encargan de guardar los cambios que se le hicieron a las listas
"""

"Dinero"

def guardarDinero():
    csvfile = open("Dinero.csv",'w',newline="")
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dinero)
        
"Productos"

def guardarProductos():
    csvfile = open("Productos.csv",'w',newline="")
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(productos)
################################################
        
"""
Esta funcion es la que guarda el reset()
"""
def LimpiarMovimientos():
    csvfile = open("Movimientos.csv",'w',newline="")
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([])
        
################################################

"""
actualizar_movimientos: resive los valores nesesarios para agragarlos a la tabla de movimientos
E: enteros
R:
S: la tabla actualizada
"""
def actualizar_movimientos(codigo,n,devolver,pago,deben):
    largo = len(movimientos) 
    trasaccion = (len(movimientos) +1)
    movimientos.append(['VE',trasaccion,time.asctime(),codigo,n,deben,pago,devolver])
    guardarmovimientos()
################################################

"""
guardar_movimientos: hace un append a la tabla de movimientos
"""
def guardarmovimientos():
    csvfile = open("Movimientos.csv",'w',newline="")
    with csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(movimientos)
        
################################################

"""
combinar_aux: funcion que busca los datos
"""
def combinar(ind):
    if ind == len(movimientos):
        return []
    P = producto1(movimientos[ind][3],0)
    return [[movimientos[ind][3], P[1], movimientos[ind][4], movimientos[ind][1],
             movimientos[ind][2], movimientos[ind][5]]] + combinar(ind + 1)

################################################

"""
producto1:busca el codigo para encontrar el nombre del producto
Esta funcion es utilizada por combinar y por resumen
"""
def producto1(codigo,indice):
    if indice == len(productos):
         return -1

    elif str(codigo) == productos[indice][0]:
        return productos[indice]
            
    return producto1(codigo, indice + 1)

################################################

def resumen(ind):
    if ind == len(movimientos):
        return []
    P = producto1(movimientos[ind][3],0)
    return [[movimientos[ind][3], P[1], movimientos[ind][4], P[6], movimientos[ind][5]]]  + resumen(ind + 1)

################################################

def Maquina():
        """
        Carasteristicas de la ventana donde se ubicara la maquina expendedora(color de fondo tamaño de la ventana,
        si se puedemaximizar o no y su titulo)
        """
        maquina = Tk()
        maquina.configure(bg = "black")
        maquina.geometry("900x680+250+5")
        maquina.resizable(width = NO, height = NO)
        maquina.title("MAQUINA / MACHINE")
        
        """
        Imagenes de los productos que posee la maquina expendedora, una imagen que simula la puerta donde se sacan
        los productos y un label con el nombre del fabricante.Tambien su respectivo label con el precio y el codigo
        """
        
        #Son 16 Productos y una iamgen que simula una puerta

        "Bebidas"

        #Producto
        Coca = Imagenes("Coke.png",(64,64))
        IMG = Label(maquina,image = Coca)
        IMG.pack()
        IMG.place(x = 50, y = 120)
        
        #Label del precio
        CocaLbl = Label(maquina, text = "1: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        CocaLbl.place(x = 51, y = 190)
        
        #Producto
        FantaN = Imagenes("FantaNaranja.png",(64,64))
        IMG1 = Label(maquina,image = FantaN)
        IMG1.pack()
        IMG1.place(x = 150, y = 120)
        
        #Label del precio
        FantaNLbl = Label(maquina, text = "9: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        FantaNLbl.place(x = 151, y = 190)

        #Producto
        FantaU = Imagenes("FantaUva.png",(64,64))
        IMG2 = Label(maquina,image = FantaU)
        IMG2.pack()
        IMG2.place(x = 250, y = 120)

        #Label del precio
        CocaLbl = Label(maquina, text = "8: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        CocaLbl.place(x = 251, y = 190)

        #Producto
        Gatorade = Imagenes("gatorade.png",(64,64))
        IMG3 = Label(maquina,image = Gatorade)
        IMG3.pack()
        IMG3.place(x = 350, y = 120)

        #Label del precio
        gatoradeLbl = Label(maquina, text = "6: ₡1000"
                        ,bg = "white",fg = "black", font =("Arial",12))
        gatoradeLbl.place(x = 351, y = 190)
        
        #Producto
        Pepsi = Imagenes("Pepsi.png",(64,64))
        IMG4 = Label(maquina,image = Pepsi)
        IMG4.pack()
        IMG4.place(x = 50, y = 230)

        #Label del precio
        PepsiLbl = Label(maquina, text = "2: ₡700"
                        ,bg = "white",fg = "black", font =("Arial",12))
        PepsiLbl.place(x = 51, y = 300)

        #Producto
        TropicalF = Imagenes("tropicalfrutas.png",(64,64))
        IMG5 = Label(maquina,image = TropicalF)
        IMG5.pack()
        IMG5.place(x = 150, y = 230)

        #Label del precio
        TropicalFLbl = Label(maquina, text = "4: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        TropicalFLbl.place(x = 151, y = 300)

        #Producto        
        Power = Imagenes("Power.png",(64,64))
        IMG6 = Label(maquina,image = Power)
        IMG6.pack()
        IMG6.place(x = 250, y = 230)

        #Label del precio
        PowerLbl = Label(maquina, text = "5: ₡1000"
                        ,bg = "white",fg = "black", font =("Arial",12))
        PowerLbl.place(x = 251, y = 300)

        #Producto        
        Sprite = Imagenes("Sprite.png",(64,64))
        IMG7 = Label(maquina,image = Sprite)
        IMG7.pack()
        IMG7.place(x = 350, y = 230)

        #LAbel del precio
        SpriteLbl = Label(maquina, text = "10: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        SpriteLbl.place(x = 351, y = 300)
        
        #Producto
        Agua = Imagenes("Agua.png",(64,64))
        IMG8 = Label(maquina,image = Agua)
        IMG8.pack()
        IMG8.place(x = 50, y = 340)

        #Label del precio
        AguaLbl = Label(maquina, text = "3: ₡700"
                        ,bg = "white",fg = "black", font =("Arial",12))
        AguaLbl.place(x = 51, y = 410)

        #Producto
        Naranja = Imagenes("naranja.png",(64,64))
        IMG9 = Label(maquina,image = Naranja)
        IMG9.pack()
        IMG9.place(x = 150, y = 340)

        #Label del producto
        NaranjaLbl = Label(maquina, text = "7: ₡700"
                        ,bg = "white",fg = "black", font =("Arial",12))
        NaranjaLbl.place(x = 151, y = 410)
        
        "Snacks"

        #Producto
        Hershey = Imagenes("Hershey.png",(64,64))
        IMG10 = Label(maquina,image = Hershey)
        IMG10.pack()
        IMG10.place(x = 250, y = 340)

        #Label del precio
        HersheyLbl = Label(maquina, text = "16: ₡1000"
                        ,bg = "white",fg = "black", font =("Arial",12))
        HersheyLbl.place(x = 251, y = 410)

        #Producto
        PringlesO = Imagenes("PringlesOriginal.png",(64,64))
        IMG11 = Label(maquina,image = PringlesO)
        IMG11.pack()
        IMG11.place(x = 350, y = 340)

        #Label del precio
        PringlesOLbl = Label(maquina, text = "13: ₡1000"
                        ,bg = "white",fg = "black", font =("Arial",12))
        PringlesOLbl.place(x = 351, y = 410)
        
        #Producto
        Snikers = Imagenes("Snikers.png",(64,64))
        IMG12 = Label(maquina,image = Snikers)
        IMG12.pack()
        IMG12.place(x = 50, y = 450)

        #Label del precio
        SnikersLbl = Label(maquina, text = "15: ₡1000"
                        ,bg = "white",fg = "black", font =("Arial",12))
        SnikersLbl.place(x = 51, y = 520)
        
        #Producto        
        TakisF = Imagenes("TakisFuego.png",(64,64))
        IMG13 = Label(maquina,image = TakisF)
        IMG13.pack()
        IMG13.place(x = 150, y = 450)
        
        TakisFLbl = Label(maquina, text = "12: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        TakisFLbl.place(x = 151, y = 520)
        
        #Producto        
        TakisX = Imagenes("Takisxplosion.png",(64,64))
        IMG14 = Label(maquina,image = TakisX)
        IMG14.pack()
        IMG14.place(x = 250, y = 450)
        
        TakisXLbl = Label(maquina, text = "11: ₡800"
                        ,bg = "white",fg = "black", font =("Arial",12))
        TakisXLbl.place(x = 251, y = 520)
        
        #Producto        
        PringlesC = Imagenes("PringlesSourCrema.png",(64,64))
        IMG15 = Label(maquina,image = PringlesC)
        IMG15.pack()
        IMG15.place(x = 350, y = 450)

        #Label del precio
        PringlesCLbl = Label(maquina, text = "14: ₡1000"
                        ,bg = "white",fg = "black", font =("Arial",12))
        PringlesCLbl.place(x = 351, y = 520)
        
        #Puerta
        puerta = Imagenes("puerta.gif",(200,100))
        IMG16 = Label(maquina,image = puerta)
        IMG16.pack()
        IMG16.place(x = 130, y = 570)

        #Label del nombre
        maquina_i = Label( maquina, text = "CE COMPANY"          
               ,bg = "light sea green",justify = "left",relief = "ridge",font = ("GOUDY STOUT",20))
        maquina_i.place(x = 80,y = 50)
        
        """
        En esta seccion se agreganron los Label y los entry para los productos y cantidades adeamas  los botones de
        aceptar y el de administrar
        """
        
        #Label Y entry de la cantidad 
        Cantidad = Label(maquina, text = "Introduzca la cantidad \n Enter the amount",
                         bg="DodgerBlue4",fg="black",font= ("Arial Black",20))
        Cantidad.place(x=500, y = 50)
        Entrada_info = Entry(maquina, width = 10, bg = "DeepSkyBlue4",font = ("Arial Ce",20))
        Entrada_info.place(x = 590, y = 150)

        #Label y entry del producto
        Productos = Label(maquina,text = "Elija el producto \n Chooose the product",
                          bg="DodgerBlue4",fg="black",font= ("Arial Black",20))
        Productos.place(x=500, y=200)
        Entrada_info1 = Entry(maquina, width = 10, bg = "DeepSkyBlue4",font = ("Arial Ce",20))
        Entrada_info1.place(x = 570, y = 300)

        #Boton de Comprar
        Comprar = Button(maquina,text = "Comprar \n Buy",bg="SkyBlue4",fg = "black",font = ("Roman",20),
                         command = lambda: ingresar_dato(int(Entrada_info.get()),(int(Entrada_info1.get()))))
        Comprar.place(x = 600, y = 350)

        #Boton de administrar
        admin = Button(maquina, text = "Administrar \n Manage",bg="SkyBlue4",fg = "black",font = ("Roman",20)
                      ,command = lambda: Password())
        admin.place(x = 580, y = 500)

        maquina.mainloop()

################################################

"""
Funcion que crea una ventana con una especie de menu utilizando diferentes botones
"""
def Administrador():
    """
    Caracteristicas de la ventana, tamaño, titulo, fondo y si se puede maximizar o no.
    """
    admin = Toplevel(bg = "deep sky blue")
    admin.geometry("500x500+500+50")
    admin.resizable(width = NO, height = NO)
    admin.title("ADMINISTRADOR")

    fondo = Fondo("administrador.gif")
    fondo1 = Canvas(admin,width = 500, height = 500)
    fondo1.pack()
    fondo1.create_image(10,10,image = fondo,anchor= NW)
    fondo1.place(x = 0, y = 0)


    """
    Esta seccion tendra unos botones que ejecutaran algunas funciones
    Boton_Cerrar: Cerrara el programa
    """
    
    #Apagar   
    Boton_Cerrar = Button(admin,text = "Close\n Cerrar",bg="SkyBlue4",fg = "red",font = ("Roman",20)
                      ,command = Cerrar)
    Boton_Cerrar.pack(pady = 20)

    #Boton del reset
    Boton_reset = Button(admin,text = "Resetear\nReset", bg = "SkyBlue4", fg = "black", font = ("Roman",20)
                         ,command = reset)
    Boton_reset.place(x = 50, y = 250)

    #Boton para el resumen de ventas
    Boton_resumen = Button(admin,text = "Resumen\nSumary", bg = "SkyBlue4", fg = "black", font = ("Roman",20)
                           ,command = reporte_resumen)
    Boton_resumen.place(x = 350, y = 250)

    #Boton del resumen detallado
    Boton_resumenD = Button(admin,text = "Resumen Detallado\nDetailed Summary", bg = "SkyBlue4",
                           command = reporte_detallado, fg = "black", font = ("Roman",20))
    Boton_resumenD.place(x = 130, y = 150)

    admin.mainloop()

################################################

"""
Password: ventana que crea la entrada y el boton para la contraseña
E: una contraseña
R: no hay
S: la funcion correct
"""
def Password():  

    bloqueo  = Toplevel(bg ="SteelBlue4")
    bloqueo.geometry("400x300+750+380")
    bloqueo.resizable(width = False, height = False)
    bloqueo.title("LOOK")
    
    """
    Label con el texto de "Ingresar la imagen", su entrada y un boton que retorna la funcion correct()
    """

    #Label
    
    Ingrese = Label(bloqueo, text = "Ingrese la contraseña\nEnter the password",bg="DodgerBlue4",
                    fg="black",font= ("Arial Black",20))
    Ingrese.place(x = 25, y = 50)

    #Entry
    
    Contraseña = Entry(bloqueo, width = 10, bg = "DeepSkyBlue4",font = ("Arial Ce",20))
    Contraseña.place(x = 125, y = 150)

    #Boton
    
    Aceptar = Button(bloqueo, text = "Aceptar\nAcept", bg = "SkyBlue4", fg = "black", font = ("Roman",20)
                , command = lambda: correct(Contraseña.get()))
    Aceptar.place(x = 150, y = 200)

    bloqueo.mainloop()

################################################

"""
En esta seccion se crea la ventana para pagar por los productos
E: los valores del subtotal,codigo y cantidad ademas de los de el valor de los billetes
R: que sean enteros
S: retorna la funcion del vuelto
"""
def Pago(subtotal,codigo,cantidad):
    """
    actualizar: resive como parametros  los spinbox y hace la operacion correspondiente
    E: los spibox y el subtotal
    R: enteros
    S: el total a dar 
    """
    def actualizar(cantidad,codigo,m100,m500,b1000,b2000):

        #Label 
        Falta = Label(pago, text = "Falta // Lack",bg="DodgerBlue4",
                        fg="black",font= ("Arial Black",20))
        Falta.place(x = 50, y = 350)

        #Operacion
        
        total1 = m100 * 100 + m500 * 500 + b1000 * 1000 + b2000 * 2000
        etiqueta1 = Label(pago, font=("Arial ",20), text="Total : ₡ " + str((total1) - subtotal)
                          ,height=1,width=20)
        etiqueta1.place(x=250,y=350)

        Pagar = Button(pago, text = "Pay\\Pagar", bg = "SkyBlue4", fg = "black", font = ("Roman",20)
                ,command =lambda: vuelto(int(total2),codigo,cantidad,Dinero100,
                                                  Dinero500,Dinero1000,Dinero2000,total2,total3,total4))
        Pagar.place(x = 600, y = 350)

        """
        Variables del vuelto y el total pagado y el subtotal
        """
        total2 = 0 #vuelto
        total3 = 0 #total
        total4 = 0 #subtotal
        total2 += total1 - subtotal
        total3 += total1
        total4 += subtotal
        
        Dinero100 = m100
        Dinero500 = m500
        Dinero1000 = b1000
        Dinero2000 = b2000
        
    pago = Toplevel()
    pago.geometry("1200x500+100+150")
    pago.resizable(width = False, height = False)
    pago.title("PAGAR / PAY")

    fondo1 = Fondo("fondo-dolares.png")
    fondo2 = Canvas(pago,width = 1200, height = 500)
    fondo2.pack()
    fondo2.create_image(0,0,image = fondo1,anchor= NW)
    fondo2.place(x = 0, y = 0)

    "Moneda"
    
    #Moneda 100
    M100_colones = Imagenes("100 colones.png",(150,150))
    IMG17 = Label(pago,image = M100_colones)
    IMG17.pack()
    IMG17.place(x = 50, y = 50)

    #spinbox
    m100 = IntVar()
    moneda100 = Spinbox(pago, from_=0,to =10,state="readonly", textvariable = m100, font =("Roman",20),
                         command = lambda:actualizar(cantidad,codigo,m100.get(),m500.get(),
                                                     b1000.get(),b2000.get())
                         ,justify = CENTER, width=13)
    moneda100.place(x = 50, y = 200)

    #Moneda 500
    M500_colones = Imagenes("500 colones.png",(150,150))
    IMG18 = Label(pago,image = M500_colones)
    IMG18.pack()
    IMG18.place(x = 300, y = 50)

    #spinbox
    m500 = IntVar()
    moneda500 = Spinbox(pago, from_=0,to =10,state="readonly", textvariable = m500, font =("Roman",20),
                        command = lambda:actualizar(cantidad,codigo,m100.get(),m500.get(),
                                                     b1000.get(),b2000.get())
                        , justify = CENTER, width=13)
    moneda500.place(x = 300, y= 200)

    "Billete"
    
    #Billete
    B1000_colones = Imagenes("1000-Colones.png",(150,150))
    IMG19 = Label(pago,image = B1000_colones)
    IMG19.pack()
    IMG19.place(x = 550, y = 50)
    
    #spinbox
    b1000 = IntVar()
    billete1000 = Spinbox(pago, from_=0,to =10,state="readonly", textvariable = b1000, font =("Roman",20),
                         command = lambda:actualizar(cantidad,codigo,m100.get(),m500.get(),
                                                     b1000.get(),b2000.get()),
                         justify = CENTER, width=13)
    billete1000.place(x = 550, y = 200)
    
    #Billete
    B2000_colones = Imagenes("2000 Colones.png",(150,150))
    IMG20 = Label(pago,image = B2000_colones)
    IMG20.pack()
    IMG20.place(x = 750, y = 50)
        
    #spinbox
    b2000 = IntVar()
    billete2000 = Spinbox(pago, from_=0,to =10,state="readonly", textvariable = b2000, font =("Roman",20),
                          command = lambda:actualizar(cantidad,codigo,m100.get(),m500.get(),
                                                     b1000.get(),b2000.get()),
                        justify = CENTER, width=13)
    billete2000.place(x = 750, y = 200)

    pago.mainloop()

################################################

"""
reporte_resumen: da un reporte resumido de ventas, con el codigo, producto,existencias, vendidas, monto
E: las tablas globales de movimientos y  productos
R: las tablas correctas
S: el resumen en una ventana nueva
"""
def reporte_resumen():

    desglose = resumen_tabla()
    """
    Caracteristicas de la ventana
    """
    resumen = Toplevel(bg="cyan4")
    resumen.geometry("800x500+100+150")
    resumen.resizable(width = False, height = False)
    resumen.title("RESUMEN / SUMMARY")

    #Tabla

    tabla = ttk.Treeview(resumen, columns=("col1","col2","col3","col4" ))
    tabla.column("#0", width=100,anchor=CENTER)
    tabla.column("col1", width=150,anchor=CENTER)
    tabla.column("col2", width=150,anchor=CENTER)
    tabla.column("col3", width=100,anchor=CENTER)
    tabla.column("col4", width=100,anchor=CENTER)
    
    tabla.heading("#0", text="Codigo//Code", anchor=CENTER)
    tabla.heading("col1", text="Descripccion//Description", anchor=CENTER)
    tabla.heading("col2", text="Cantidad//Amount", anchor=CENTER)
    tabla.heading("col3", text="Vendidas//Sold", anchor=CENTER)
    tabla.heading("col4", text="Monto//Amount", anchor=CENTER)
    

    i = 0
    while i!= len(desglose):
        tabla.insert("", END, text=desglose[i][0], values=(desglose[i][1:]))
        i += 1

    tabla.pack()
    tabla.place(x=100,y=100)

    resumen.mainloop()

################################################
"""
reporte_detallado: da un reporte detallado de ventas, con el codigo, producto,#Transaccion, fecha, cantidad,
monto
E: las tablas globales de movimientos y  productos
R: las tablas correctas
S: el detalle de ventas en una ventana nueva
"""
def reporte_detallado():

    datos = combinar(0)
    
    """
    Caracteristicas de la ventana
    """    
    detalle = Toplevel(bg="cyan4")
    detalle.geometry("800x500+100+150")
    detalle.resizable(width = False, height = False)
    detalle.title("Detail / DETAIL")


    #Tabla
    
    tabla = ttk.Treeview(detalle, columns=("col1","col2","col3","col4","col5" ))
    tabla.column("#0", width=100,anchor=CENTER)
    tabla.column("col1", width=150,anchor=CENTER)
    tabla.column("col2", width=110,anchor=CENTER)
    tabla.column("col3", width=180,anchor=CENTER)
    tabla.column("col4", width=150,anchor=CENTER)
    tabla.column("col5", width=100,anchor=CENTER)
    
    tabla.heading("#0", text="Codigo//Code", anchor=CENTER)
    tabla.heading("col1", text="Descripccion//Description", anchor=CENTER)
    tabla.heading("col2", text="Cantidad//Amount", anchor=CENTER)
    tabla.heading("col3", text="# Transaccion//# Transaction", anchor=CENTER)
    tabla.heading("col4", text="Fecha//Date", anchor=CENTER)
    tabla.heading("col5", text="Monto//Amount", anchor=CENTER)
    

    i = 0
    while i!= len(datos):
        tabla.insert("", END, text=datos[i][0], values=(datos[i][1:]))
        i += 1

    tabla.pack()
    tabla.place(x=5,y=100)

    detalle.mainloop()

################################################
    
"""
Funcion que resive un argumento entero
E: un numero
R: entero
S: una funcion auxiliar
"""
def ingresar_dato(n,codigo):
        if  n <= 15 and codigo <= 16 :
             return producto(n, codigo, 0)
        else:
            messagebox.showerror( "Error","El numero de productos debe ser menor a\n"
                                  "16,el codigo debe ser entre 1 a 16"
                                 "\n\nThe number of products must be less"
                                 "than 1, the code must be between 1 to 16")
            return "Error, el dato no se pudo convertir"

"""
producto: resive n, codigo, indice
E: numeros enteros
R: previemente verificada en la funcion anteror
S: Sì hay productos suficientes
"""
def producto(n,codigo,indice):
    if indice == len(productos):
         messagebox.showerror("Error","El producto no esta en la maquina\n\n"
                             "The product is not in the machine")
         return False,False,-1

    elif str(codigo) == productos[indice][0] and int(productos[indice][2]) == 0:
        messagebox.showerror("Producto agotado//Sold out","Ya no quedan productos a la venta\n\n"
                            "There are no more products for sale")
    
    elif str(codigo) == productos[indice][0] and int(productos[indice][2]) < n:
        messagebox.showerror("Error","Solo quedan "+productos[indice][2]+"\n\n"
                            "Only left "+productos[indice][2])
        return True,False,indice

    elif str(codigo) == productos[indice][0] and int(productos[indice][2]) >= n:
        total(n,codigo,0,n)
        return True,True,indice
            
    return producto(n, codigo, indice + 1)
                            
################################################
"""
total: total a pagar
E: cantidad de articulos
R: una cantidad adecuada(permitida)
S: el total
"""
def total(cantidad,codigo,subtotal,cantidad2):
    if cantidad == 0:
        Pago(subtotal,codigo,cantidad2)
        return "Listo, cantidad a pagar lista"
    elif  cantidad == 1:
        subtotal = int(productos[codigo-1][5])
        return total(cantidad - 1, codigo,subtotal,cantidad2)
    else:
        subtotal = int(productos[codigo-1][5]) * cantidad
        return total(cantidad - cantidad, codigo,subtotal,cantidad2)
    
################################################

"""
actualizar: valida primero que se alla pagado por completo, y despues si el vuelto es cero retornara una actualizacion
de la lista de dinero, pero si es mayor retornara la funcion que dara el vuelto.
E: numeros enteros
"""
def vuelto(vuelto,codigo,cantidad,Dinero100,Dinero500,Dinero1000,Dinero2000,devolver,pago,debe):
    if vuelto < 0:
        messagebox.showerror("Error", "Aun nos terminado de pagar\n\n"
                            "You haven't finished paying yet")
        return "Error, no se ha terminado de pagar"
    elif vuelto == 0:
        messagebox.showinfo("Gracias//Thanks","Thaks for buying\n\n"
                            "Gracias por comprar")
        Sumar(Dinero100,Dinero500,Dinero1000,Dinero2000)
        actualizar_movimientos(codigo,cantidad,devolver,pago,debe)
        cambiarcantidad(codigo,cantidad,0)
        return Cerrar()
    else:
        Sumar(Dinero100,Dinero500,Dinero1000,Dinero2000)
        vuelto_aux(vuelto,codigo,cantidad,0,0,0,0,vuelto,devolver,pago,debe)
        return "Listo"

"""
Sumar: resive los datos con los cuales se pagaron el productos y los suma
E: los datos con los cuales se pagaron
R: enteros
R: guardarDinero
"""
def Sumar(Dinero100,Dinero500,Dinero1000,Dinero2000):
        if Dinero100 == 0 and Dinero2000 == 0 and Dinero500 == 0 and Dinero100 == 0:
            guardarDinero()
            return True
        elif Dinero2000 > 0:
            dinero[3][2] = str(int(dinero[3][2]) + Dinero2000)
            return Sumar(Dinero100,Dinero500,Dinero1000,Dinero2000 - Dinero2000) 
        elif Dinero1000 > 0:
            dinero[2][2] = str(int(dinero[2][2]) + Dinero1000)
            return Sumar(Dinero100 - Dinero100,Dinero500,Dinero1000 - Dinero1000 ,Dinero2000) 
        elif Dinero500 > 0:
            dinero[1][2] = str(int(dinero[1][2]) + Dinero500)
            return Sumar(Dinero100,Dinero500 - Dinero500,Dinero1000,Dinero2000)        
        elif Dinero100 > 0:
            dinero[0][2] = str(int(dinero[0][2]) + Dinero100)
            return Sumar(Dinero100 - Dinero100,Dinero500,Dinero1000,Dinero2000)

"""
Funcuion que verifica cuanto debe de otorgar de vuelto.
E: El numero de vuelto que debe de dar
R: Enteros
S: El vuelto de una manera en la que se le da prioridad a las denominaciones mas altas
"""
def vuelto_aux(vuelto,codigo,n, mil, dosmil, quinientos, cien, total,devolver,pago,debe):
    if vuelto == 0:
        messagebox.showinfo("Vuelto//Turned","Su vueto es de//You return is from:\t\n"
                            + "₡2000:\t" + str(dosmil)+"\n₡1000:\t" + str(mil) +
                            "\n₡500:\t" + str(quinientos) + "\n₡100:\t" + str(cien) +
                            "\n\nTotal:\t" + "₡" + str(total))
        vendido(codigo,n,mil,dosmil,quinientos,cien,devolver,pago,debe)
        return True
    elif vuelto != 0 and vuelto >= 2000 and int(dinero[3][2]) >= 1:
        return vuelto_aux(vuelto - 2000, codigo,n, mil, dosmil + 1, quinientos, cien, total,devolver,pago,debe)
    elif vuelto != 0 and vuelto >= 1000 and int(dinero[2][2]) >= 1:
        return vuelto_aux(vuelto - 1000, codigo,n, mil + 1, dosmil, quinientos, cien, total,devolver,pago,debe)
    elif vuelto != 0 and vuelto >= 500 and int(dinero[1][2]) >= 1:
        return vuelto_aux(vuelto - 500, codigo,n, mil, dosmil, quinientos + 1, cien, total,devolver,pago,debe)
    elif vuelto != 0 and vuelto >= 100 and int(dinero[0][2]) >= 1 :
        return vuelto_aux(vuelto - 100, codigo,n, mil, dosmil, quinientos, cien + 1, total,devolver,pago,debe)
    elif vuelto != 0 and vuelto >= 100 and int(dinero[0][2]) < 1 :
        messagebox.showerror("Error","No hay vuelto suficiente\n\n"
                            "There is not enough return")
        return "Error, no hay vuelto suficiente"
    else:
        messagebox.showerror("Error","Algo salio mal\n\n"
                            "Something went wrong")
        return "Error, algo sucedio con el vuelto"
    
################################################
   
"""
vendido: funcion que se retornara cuando el usuario pagara y se le diera vuelto si este fuese nesesario, reescribira
en los archivos de texto de movimientos, dinero y productos.
E: los datos del vuelto, la lista de productos y lo pagado
R: los datos se van a convertir a un valor apropiado para su manipulacion
S: El arreglo a cada una de las listas
"""
def vendido(codigo,n,mil,dosmil,quinientos,cien,devolver,pago,deben):
    if mil == 0 and dosmil == 0 and quinientos == 0 and cien == 0:
        cambiarcantidad(codigo,n,0)
        guardarDinero()
        actualizar_movimientos(codigo,n,devolver,pago,deben)
        Cerrar()
        return True
    elif dosmil > 0:
        dinero[3][2] = str(int(dinero[3][2]) - dosmil)
        return vendido(codigo,n, mil, dosmil - dosmil, quinientos, cien,devolver,pago,deben) 
    elif mil > 0:
        dinero[2][2] = str(int(dinero[2][2]) - mil)
        return vendido(codigo,n, mil - mil, dosmil, quinientos, cien,devolver,pago,deben) 
    elif quinientos > 0:
        dinero[1][2] = str(int(dinero[1][2]) - quinientos)
        return vendido(codigo,n, mil, dosmil, quinientos - quinientos,cien,devolver,pago,deben)        
    elif cien > 0:
        dinero[0][2] = str(int(dinero[0][2]) - cien)
        return vendido(codigo,n, mil, dosmil, quinientos, cien - cien,devolver,pago,deben)
        
################################################
        
"""
cambiarcantidad: actualiza la cantidad de productos
E: enteros
R: que sea la lista correcta
S: la lista pructos actualizada
"""
def cambiarcantidad(codigo,cantidad,indice):
    if indice == len(productos):
         messagebox.showinfo("Error","Hubo un problema\n\n"
                             "There was a problem")
         Cerrar()
         return False
    elif str(codigo) == productos[indice][0]:
        productos[indice][2] = str(int(productos[indice][2]) - cantidad)
        productos[indice][6] = str(int(productos[indice][6]) + cantidad)
        guardarProductos()
        return True
            
    return cambiarcantidad(codigo,cantidad, indice + 1)


################################################

"""
Se inicializa las funciones para leer los archivos de texto creados
"""
leerP()
leerM()
leerD()
Maquina()

