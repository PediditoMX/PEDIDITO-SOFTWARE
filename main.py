"""
PEDIDITO SOFTWARE

Author: PolitropicMX
"""
### LIBRERIAS

import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from threading import Thread
from cronometro import CronometroApp
import time
from agregar_pedido_win import Agregar_pedido
from pendientes_win import Pendientes_class
from analisis_win import Analisis_class
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
import openpyxl
from PIL import Image, ImageTk
from tkinter import Label, PhotoImage
from palettes import dusk
from Inicio_sesion import Iniciar_sesion

#### FUNCIONES DEL PROGRAMA Y OTROS ARCHIVOS

#       ###     #          #
#      #   #   #   #   #    #
#     #       #     # #      #
#   #######   #      #       #
#     #       #     # #      #
#     #       #    #   #     #
#     #        #  #     #   #
#     #         #          #


## El CRONOMETRO CUANDO UNA ORDEN SE INICIA
        
## BUTTON FUNC; ACTIVATED WHEN PRESSED
def agregar():
    agregar_ventana = Agregar_pedido(root,treeview)
##    agregar_ventana.draw()
    # DIBUJATIVA
## RETURN FUNC; THIUS IS THE GRIDGE BETWEEN THAT WINDOW AN THIS WINDOW
    
    
def analisis_ventana():
    analisis_win = Analisis_class(root)
    analisis_win.draw()

def mostrar_dicc(tree, diccionario, parent=""):
    for i,fila in enumerate(diccionario):
        if parent == "btn-add":# 
            tree.insert("", '0',text=fila[0], values=fila[1:])
        else:
            tree.insert("", 'end',text=fila[0], values=fila[1:])
        
def leer_excel(ruta_archivo, nombre_hoja, rango):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja)
    print(df)
    # Seleccionar el rango específico
    df_rango = df.loc[rango[0]:rango[1]]

    # Convertir el DataFrame a un diccionario
    datos_diccionario = df_rango.to_dict(orient='records')

    return datos_diccionario

def extraer_informacion_desde_rango(hoja, rango):
    datos_extraidos = []

    # Obtener las celdas en el rango especificado
    celdas = hoja[rango]
    
    # Iterar sobre las celdas en el rango
    for fila in reversed(celdas):
        fila_datos = [celda.value for celda in fila]
        datos_extraidos.append(fila_datos)

    return datos_extraidos

def actualizar_fecha(etiqueta1,etiqueta2):
    fecha_hora_actual = datetime.now()
    hora_str = fecha_hora_actual.strftime("%H:%M:%S")
    fecha_str = fecha_hora_actual.strftime("%d de %B %Y\n ")
    etiqueta1.config(text=f"{hora_str}")
    etiqueta2.config(text=f"{fecha_str}")
    root.after(1000, lambda: actualizar_fecha(etiqueta1,etiqueta2))  # Actualizar cada 1000 milisegundos (1 segundo)
    
def draw(dashboard,nombre):
    for i,widget in enumerate(dashboard):
        if len(widget) == 1:
            pass
        else:
            if nombre == "0":
                widget[0].grid(row=widget[1][0],column=widget[1][1],padx= widget[1][2],pady = widget[1][3],sticky= widget[1][4])
            else:
                pass



## Funcion usada para el --boton:Terminar orden--

# Funcion para sumar los numeros y mostrar los resultdos
def sumar_conceptos(event):
    pass

# Función para restar los números y mostrar el resultado
def restar_numeros(event):
    try:
        costo = float(main_costo_cli.get())
        paga_con = float(main_paga_con.get())
        tarifa = float(main_tarifa_cli.get())
        costo_total = costo + tarifa
        main_total_cli.set(costo_total)
        resultado = paga_con - costo_total
        main_cambio_cli.set(resultado)
        suma = 0
        for i,j in enumerate(costos_unitarios):
            costo = j.get()
            suma += costo*cantidades[i]
    except ValueError:
        # Manejar la excepción si los valores ingresados no son números
        pass
def imagelabel(name,lista,parent,coor):
    img = Image.open(name)
    img_tk = ImageTk.PhotoImage(img)# Convertir la imagen para tkinter
    lista.append([tk.Label(parent, image=img_tk),coor])# Crear un Label dentro del Frame para mostrar la imagen
    return lista    


def comprobar(activity):
    erase
    draw(activity,"0")

##### AQUI EMPIEZA LA APP DE PEDIDITO VENTANA PRINCIPAL #####
# #    #    ##     ###   #    #  
# ##  ##   #  #     #    ##   #  
# # ## #  #    #    #    # #  #  
# #    #  ######    #    #  # #  
# #    #  #    #    #    #   ##  
# #    #  #    #    #    #    #  
# #    #  #    #   ###   #    # 

    
##### MAPA JERARQUICO
## root
##    cuaderno
##       hojas: encabezados = ['Principal','Buscar','Mapa']
##          paginas
##             opciones_labelframes
##                opciones_widgets_1
##             pizarra


# VENTANA PRINCIPAL
## VENTANA
root = tk.Tk()
root.title("PEDIDITO SYSTEMS TECHNOLOGY by Fernando López V.")
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("520x600")

usuario = "Xtrim"

usuario = tk.StringVar()
contrasena =tk.StringVar()
usuario.set("Xtrim")
contrasena.set("Buba69")

inicio_sesion = []
inicio_sesion.append([tk.Frame(root,bg=dusk[4]),(0,0,50,50,"nsew")])# 0
inicio_sesion.append([tk.Label(inicio_sesion[0][0], text="Ingrese al Sistema\nPEDIDITO SOFTWARE"),(0,0,10,10,"nsew")])# 1
inicio_sesion.append([tk.Button(inicio_sesion[0][0],text=">",font=("Helvetica",20),fg=dusk[1],bg=dusk[3],command=comprobar),(3,0,0,(20,0),"")])#10
inicio_sesion.append([tk.Entry(inicio_sesion[0][0],textvariable=usuario,font=("Helvetica",20),fg=dusk[2],bg=dusk[4] ),(1,0,0,20,"")])#10
inicio_sesion.append([tk.Entry(inicio_sesion[0][0],textvariable=contrasena,font=("Helvetica",20),fg=dusk[1],bg=dusk[4] ),(2,0,0,20,"")])#10

# Notebook
dashboard = []
dashboard.append([ttk.Notebook(root),(0,0,0,0,"")])# 0
encabezados = ['Principal','Buscar','Mapa']
for i,encabezado in enumerate(encabezados):# 3*2= 6
    dashboard.append([tk.Frame(dashboard[0][0],bg=dusk[4])])#1, Se añaden 3 frames por cada encabezado
    dashboard[0][0].add(dashboard[2*i+1][0], text=encabezado)# En el frame que cree atras, le agrego el nombre 
    dashboard.append([tk.Frame(dashboard[2*i+1][0],bg=dusk[4]),(0,0,10,10,"")])#2, luego se crea un frame hijo en hojas[1]
fecha_actual = datetime.now()
dashboard.append([tk.Label(dashboard[1][0],text=fecha_actual,font=("Helvetica",50),fg=dusk[1],bg=dusk[4]),(1,0,5,5,"")])# 7
dashboard.append([tk.Label(dashboard[1][0],text=fecha_actual,font=("Helvetica",25),fg=dusk[2],bg=dusk[4]),(2,0,5,5,"")])# 8
dashboard.append([tk.Frame(dashboard[1][0],bg=dusk[3]),(0,1,5,5,"")])# 9
dashboard.append([tk.Button(dashboard[9][0],text="( + )",font=("Helvetica",20),fg=dusk[0],bg=dusk[3],command=agregar),(0,0,0,0,"")])#10
dashboard.append([tk.Button(dashboard[9][0],text="( X )",font=("Helvetica",20),fg=dusk[0],bg=dusk[3]),(0,1,0,0,"")])#11
dashboard.append([tk.Label(dashboard[1][0],text=f"Usuario: {usuario}",font=("Helvetica",30),fg=dusk[4],bg=dusk[0]),(0,0,0,0,"")])# 12
dashboard = imagelabel("pedidito_fondo.jpeg",dashboard,dashboard[1][0],(3,0,0,0,"nsew"))# 13

# ACTIVITY 2: TERMINAR ORDEN
actualizar_fecha(dashboard[7][0],dashboard[8][0])

draw(inicio_sesion,"0")

## Strings del dia
main_ordenes_del_dia = tk.IntVar()


# ######  #####   ######  ######  #    #   ###   ######  #    #  
#   #     #    #  #       #       #    #    #    #       #    #  
#   #     #    #  #       #       #    #    #    #       #    #  
#   #     #####   #####   #####   #    #    #    #####   #    #  
#   #     #   #   #       #       #    #    #    #       # ## #  
#   #     #    #  #       #        #  #     #    #       ##  ##  
#   #     #    #  ######  ######    ##     ###   ######  #    #

# Create a Frame for the Treeview
treeFrame = tk.Frame(dashboard[3][0])
treeFrame.grid(row=1, column=0)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")
treeScrollx = ttk.Scrollbar(treeFrame,orient="horizontal")
treeScrollx.pack(side="bottom", fill="x")
encabezados = ["N° de Pedido","Fecha","Hora del pedido","Nombre del cliente","N° de Contacto","Recoleccion","Entrega","Producto","Paga con…","Costo del pedido","Tarifa","Cobro total","Dinero entregado a repartidor para compra","$ entregado al repartidor para cambio","$ total dado al repartidor","$ total recibido por el repartidor"]  

# Treeview
columnas = [i for i in range(1,len(encabezados))]
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, xscrollcommand = treeScrollx.set, columns=columnas, height=30)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)
treeScrollx.config(command=treeview.xview)


# Treeview headings
for i, j in enumerate(encabezados):
    if i == 0:
        treeview.column("#0", width=100)
        treeview.heading("#0", text=j, anchor="center")
    else:
        treeview.heading(i, text=j, anchor="center")
        treeview.column(i, anchor="w", width=100)

# ######  #    #   ####   ######  #       
# #        #  #   #    #  #       #       
# #         ##    #       #       #       
# #####     ##    #       #####   #       
# #         ##    #       #       #       
# #        #  #   #    #  #       #       
# ######  #    #   ####   ######  ######

# Ejemplo de uso
ruta_archivo_excel = 'PEDIDITO_DB.xlsx'
nombre_hoja_excel = 'BASE_PEDIDITO'
rango_a_extraer = 'A2:K150'  # Por ejemplo, desde A1 hasta C10
libro = openpyxl.load_workbook(ruta_archivo_excel)# Cargar el libro de trabajo (workbook)
hoja = libro[nombre_hoja_excel]# Acceder a una hoja específica
informacion_extraida = extraer_informacion_desde_rango(hoja, rango_a_extraer)# Extraer información desde el rango especificado
pedidos_totales = len(informacion_extraida) # int: numero de filas del archivo excel leido
print("ingreso de base de datos a PEDIDITO SOFTWARE")
print(informacion_extraida[1:10])# Debe estar llena la informacion extraida del excel
mostrar_dicc(treeview,informacion_extraida)
# Cerrar el libro después de usarlo
libro.close()

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()

# #######                    
# #           #              
# #                 #####    
# ######     ##     #    #   
# #           #     #    #   
# #           #     #    #   
# #         #####   #    #





