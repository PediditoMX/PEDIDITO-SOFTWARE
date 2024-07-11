#    #                       #                                                    #####                                                              #                     
#   # #                      #           #                                          #                                            #                   #                     
#  #   #   #####      #####  #                 #    #     ###      #####            #     #####    #####      ###    #####      ###      ###         #     ###      #####  
# #     #  #    #    #       #####      ##     #    #    #   #    #                 #     # # #    #    #    #   #   #    #      #          #    #####    #   #    #       
# #######  #         #       #    #      #     #    #   #     #    #####            #     # # #    #    #   #     #  #           #       #####  #    #   #     #    #####  
# #     #  #         #       #    #      #      #  #     #   #         #            #     # # #    #####     #   #   #           #      #    #  #    #    #   #         #  
# #     #  #          #####  #    #    #####     ##       ###     #####           #####   #   #    #          ###    #            ##     #####   #####     ###     ##### 
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from cronometro import CronometroApp
import openpyxl
from threading import Thread
from palettes import dusk
import time

### UN WIDGET SE COMPONE DE 4 LINEAS DE CODIGO
### EL PASO CERO ES CREAR UN OBJETO QUE ALMACENE UN VALOR DE UN WIDGET, PERTENECIENTE A LA CLASE TKINTER, COMO StringVar()
### PRIMERO SE DECLARA EL WIDGET, INDICANDO EL TEXTO QUE CMOSTRARÁ Y EL RECIPIENTE QUE LO CONTENDRÁ
### Y LA SEGUNDA LINEA INDICA EN QUÉ POSICIÓN ESTARÁ EN EL WIDGET PADRE
### LA TERCERA, QUE AL IGUAL A LA LINEA CERO SON OPCIONALES DEPENDIENDO EL WIDGET

# EJEMPLO DE UN PEDIDITO
##reyes,
##1 coca 12/34,
##3 elotes 23/34.
##irma,
##1 platano 1/2,
##3 leches lala 20,
##4 papayas 20.
##Total real:36,
##Cobro total:70,
##Tarifa:10,
##Propina:5,
##Final:85


class Agregar_pedido:
        
    def __init__(self,root,tree):
        ### ABOUT
        ### ESTA ES UNA FUNCION CONSTRUCTOR DONDE SE DECLARAN LOS WIDGETS QUE FORMAN LA VENTANA
#  #####                                                                                             
# #     #                                #                                   #                       
# #          ###    #####      #####    ###    #####    #    #     #####    ###      ###    #####    
# #         #   #   #    #    #          #     #    #   #    #    #          #      #   #   #    #   
# #        #     #  #    #     #####     #     #        #    #    #          #     #     #  #        
# #     #   #   #   #    #         #     #     #        #    #    #          #      #   #   #        
#  #####     ###    #    #    #####       ##   #         #####     #####      ##     ###    #
##ABOUT ME
##root: widget que sera padre de esta ventana
##tree: es un objeto tk.treeview() enviado del archivo padre

#    #              #     #                                      #          ##                       
#   ##              #     #                       #              #           #                       
#    #              #     #    ###    #####               ###    #           #       #####    #####  
#    #      #####    #   #        #   #    #     ##          #   #####       #      #    #   #       
#    #               #   #     #####  #           #       #####  #    #      #      #####     #####  
#    #                # #     #    #  #           #      #    #  #    #      #      #             #  
#  #####               #       #####  #         #####     #####  #####     #####     #####   #####   
           
        
        self.costo_total = 0
        self.precio_venta = 0
        self.tree = tree# el treeview de la ventana principal o ventana padre
        ## CODIGO PARA ESTRAER FECHAY HORA        
        self.opciones_var = []
        self.lista_de_tiendas = {
                        "1":"Reyes",
                        "2":"Tacos Beto",
                        "3":"Hamburguesas al carbon 2",
                        "4":"Postres la jaula",
                        "5":"Tacos de arrachera",
                        "6":"Crepas",
                        "7":"Tacos birria",
                        "8":"Banderillas luigi",
                        "9":"Panaderia los 2000",
                        "10":"Carnitas prados",
                        "11":"Azcarbon",
                        "12":"Fonda los 50",
                        "13":"Tienda la lupita",
                        "14":"Tacos foodtruck",
                        "15":"purificadora rosa",
                        "16":"Farmacia Abuelitos",
                        "17":"Supercito",
                        "18":"Carniceria los rucos",
                        "19":"polleria bachoco",
                        "20":"comida para llevar orange",
                        "21":"farmacia bambi",
                        "22":"pollo la corcholata",
                        "23":"la carniceria el chico",
                        "24":"Tienda Irma",
                        "25":"Huaraches",
                        "26":"Papeleria fake",
                        "27":"Optica",
                        "28":"Panaderia francisco",
                        "29":"Listones Ruca",
                        "30":"EdgarOnline",
                        "31":"Donas coche",
                        "32":"OXXO",
                        "33":"tacos don dani",
                        "34":"Carniceria Angel los putos",
                        "35":"Tienda Angel",
                        "36":"Tienda las girlfriend",
                        "37":"Ferreteria Prados",
                        "38":"Magnum",
                        "39":"Cocina Claudette",
                        "40":"Barbacha",
                        "41":"Tienda Pet",
                        "42":"Purificadora Iglesia",
                        "43":"Recauderia iglesia",
                        "44":"Serranita",
                        "45":"Tienda Israel",
                        "46":"Chilaquiles Israel",
                        "47":"Cerrajero el Verde",
                        "48":"El verduras Cetis 33",
                        "49":"Helados Cetis 33",
                        "50":"OfficeDepot",
                        "51":"Tacos de carnitas el rosario",
                        "52":"Abarrotes Oasis",
                        "53":"Soriana",
                        "54":"Tortas Soriana",
                        "55":"Hamburguesas olvidadas",
                        "56":"Cerrajeria",
                        "57":"Tacos de Canasta",
                        "58":"Local de Frutas",
                        "59":"TownCenter Rosario",
                        "60":"BbqCronch",
                        "61":"Mandrake",
                        "62":"Aquacliva",
                        "63":"Pan chino",# Rancho la esmeralda
                        "64":"Quesadillas la curva",
                        "65":"Hamburguesas al carbon",
                        "66":"Antojitos Mario"
                        }
            
## TODOS LOS WIDGETS A USAR ------------------------------------------------------------------------------------------------------------------------------------

        
#  #####                                                #     #                      #              
# #     #     #                 #                       #     #                      #              
# #          ###    #####             #####      #####  #     #    ###    #####      #       #####  
#  #####      #     #    #     ##     #    #    #    #   #   #        #   #    #            #       
#       #     #     #           #     #    #     #####   #   #     #####  #                  #####  
# #     #     #     #           #     #    #        #     # #     #    #  #                      #  
#  #####       ##   #         #####   #    #    #####      #       #####  #                 #####   

        # --TIEMPO
        self.ahora = datetime.now()# Obtener el tiempo de ahora
        self.fecha_y_hora = self.ahora.strftime("%Y-%m-%d %H:%M:%S")
        self.fecha, self.hora = self.fecha_y_hora.split(' ')
        self.main_fecha_cli = tk.StringVar()
        self.main_hora_cli = tk.StringVar()
        # -- PRIMERA ACTIVITY
        self.cuadernito = tk.StringVar() # Recoje la primer orden escrita 
        # -- SEGUNDA ACTIVITY
        self.main_name_cli = tk.StringVar()# 5
        self.main_num_cli = tk.StringVar()# 7
        self.main_recoleccion = tk.StringVar()
        self.main_direccion_cli = tk.StringVar()# 3
        self.main_orden_cli = tk.StringVar()
        self.main_paga_con = tk.StringVar()
        self.main_costo_cli = tk.StringVar()
        self.main_tarifa_cli = tk.StringVar()# 9
        self.main_total_cli = tk.StringVar()
        self.main_cambio_cli = tk.StringVar()
        self.main_precio_final = tk.StringVar()
        self.main_metodo_pago = tk.StringVar()
        self.main_cronometro_cli = [] # Debe ser una lista por que almacena diferentes tk.StringVar()
        self.main_cronometro_cli.append(tk.StringVar())
        # -- VENTANA EDITAR
        self.cantidad = tk.StringVar()
        self.nombre = tk.StringVar()
        self.costo = tk.StringVar()
        self.precio = tk.StringVar()

        self.palette = dusk
        self.backgrounds = 5
        self.labelframes = 3
        self.buttons = 2
        self.frames = 4
##        self.colors = [
##            ""
##            ]

#    #                                                                                      
#   # #                #        #                 #        #        #                       
#  #   #     #####    ###             #    #              ###               #####    #####  
# #     #   #          #       ##     #    #     ##        #       ##      #    #   #       
# #######   #          #        #     #    #      #        #        #      #####     #####  
# #     #   #          #        #      #  #       #        #        #      #             #  
# #     #    #####      ##    #####     ##      #####       ##    #####     #####   #####   

        ## VENTANA
        self.root = tk.Toplevel(root,bg=self.palette[self.backgrounds])# 0

        ##      ESTRUCTURA DE LA VENTANA
    
##        ## FRAME
##        # ESTRUCTURA DEL segunda_activity
##        p_a[0]:LB"Detalles del pedido"(0,1,3,3
##            p_a[2]:LB"Direccion de entrega"
##                p_a[3]:En
##            p_a[4]:LB"Nombre cliente"
##                p_a[5]:En
##            p_a[6]:LB"Nombre cliente"
##                p_a[7]:En
##            p_a[8]:LB"Nombre cliente"
##                p_a[9]:En
##            p_a[12]:LB"Metodo de pago"
##                p_a[13]
##                p_a[14]
##                p_a[15]
##                p_a[15]:LB"No ha selecciónado\n metodo de pago"
##                p_a[16]:F
##            p_a[21]:LB""
##                p_a[22]:B"Guardar"
##                p_a[23]:B"Cancelar"
##        p_a[1]:L"fecha y hora"
##        p_a[10]:LB"Productos"
##            p_a[11]:Textbox
        
        self.primera_activity = []
        self.primera_activity.append([tk.LabelFrame(self.root, text="Anotar Orden",bg=self.palette[self.labelframes]),(0,0,20,60,"nsew")])# 0
        self.primera_activity.append([tk.Text(self.primera_activity[0][0], height=20, width=60),(0,0,10,10,"")])# 1
        self.primera_activity[1][0].insert(tk.END,"""reyes,1 coca 12/34,3 elotes 23/34.irma,1 platano 1/2,3 leches lala 20,4 papayas 20.Total real:36,Cobro total:70,Tarifa:10,Propina:5,Final:85""")
        self.primera_activity.append([tk.Button(self.primera_activity[0][0], text="Siguiente",command=self.siguiente_f,bg=self.palette[self.buttons]),(1,0,0,0,"")])
        self.draw(self.primera_activity,"0")
        
        self.segunda_activity = []
        self.segunda_activity.append([tk.LabelFrame(self.root, text="Detalles del Pedido",bg=self.palette[self.labelframes]),(1,0,3,3,"nsew")])# 0
        self.segunda_activity.append([tk.Label(self.root,text=self.fecha_y_hora,bg=self.palette[self.labelframes]),(0,0,5,5,"nwes")])# 1
        #DIRECCION
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[0][0], text="Dirección de Entrega",bg=self.palette[self.labelframes]),(0,0,0,0,"nwes")])# 2
        self.segunda_activity.append([ttk.Entry(self.segunda_activity[2][0],textvariable=self.main_direccion_cli ),(0,0,5,5,"ew")])# 3
        self.segunda_activity[len(self.segunda_activity)-1][0].insert(0, "Purisima 55")
        self.segunda_activity[len(self.segunda_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.segunda_activity[3][0]))# Asociar la función borrar_texto al evento clic
        #NOMBRE 
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[0][0], text="Nombre Cliente" ,bg=self.palette[self.labelframes]),(0,1,5,5,"nwes")])# 4
        self.segunda_activity.append([ttk.Entry(self.segunda_activity[4][0],textvariable=self.main_name_cli),(0,0,0,0,"ew")])# 5
        self.segunda_activity[len(self.segunda_activity)-1][0].insert(0, "Tierno")
        self.segunda_activity[len(self.segunda_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.segunda_activity[5][0]))# Asociar la función borrar_texto al evento clic
        #NUMERO
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[0][0], text="Numero celular" ,bg=self.palette[self.labelframes]),(1,0,0,0,"nsew")])# 6
        self.segunda_activity.append([ttk.Entry(self.segunda_activity[6][0],textvariable=self.main_num_cli),(0,0,0,0,"nsew")])# 7
        self.segunda_activity[len(self.segunda_activity)-1][0].insert(0, "5510293483")
        self.segunda_activity[len(self.segunda_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.segunda_activity[7][0]))# Asociar la función borrar_texto al evento clic
        #TARIFA
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[0][0], text="Tarifa $MXN" ,bg=self.palette[self.labelframes]),(1,1,0,0,"nswe")])# 8
        self.segunda_activity.append([ttk.Entry(self.segunda_activity[8][0],textvariable=self.main_tarifa_cli),(0,0,0,0,"ew")])# 9
        self.segunda_activity[len(self.segunda_activity)-1][0].insert(0, 10)
        self.segunda_activity[len(self.segunda_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.segunda_activity[9][0]))# Asociar la función borrar_texto al evento clic
        #Orden
        self.segunda_activity.append([tk.LabelFrame(self.root, text="Lista de WhatsApp",bg=self.palette[self.labelframes]),(2,0,0,0,"")])# 10
        self.segunda_activity.append([tk.Text(self.segunda_activity[10][0], height=10, width=60),(0,0,0,0,"")])# 11
        self.segunda_activity[11][0].insert(tk.END,"""reyes,1 coca 12/34,3 elotes 23/34.irma,1 platano 1/2,3 leches lala 20,4 papayas 20.Total real:36,Cobro total:70,Tarifa:10,Propina:5,Final:85""")

        # Create a Frame for the Radiobuttons
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[0][0], text="Metodo de Pago" ,bg=self.palette[self.labelframes]),(2,0,0,0,"nsew")])# 12
        # Radiobuttons
        self.metodos_de_pago = ["Efectivo","Transferencia"]
        self.var_metodos_de_pago = tk.StringVar()
        self.var_metodos_de_pago.set(None)
        for i,metodo in enumerate(self.metodos_de_pago):# 13-14
            self.segunda_activity.append([tk.Radiobutton(self.segunda_activity[12][0], text=metodo, variable=self.var_metodos_de_pago, value=metodo, command = self.metodo_pago_func,bg=self.palette[self.buttons]),(i,0,0,0,"")])# 13
        self.segunda_activity.append([tk.Label(self.segunda_activity[12][0], text="No ha selecciónado\n metodo de pago"),(0,1,0,0,"")])# 15
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[12][0],text="Paga con"),(1,1,0,0,"")])# 16
        self.paga_con = tk.StringVar()
        self.segunda_activity.append([tk.Entry(self.segunda_activity[12][0],textvariable=self.paga_con),(2,1,0,0,"")])# 17
        self.segunda_activity.append([tk.Label(self.segunda_activity[12][0], text= f"Numero de Tarjeta:\nXXXX-XXXX-XXXX-XXXX",bg="#FFFF00"),(3,1,20,20,"")])# 18
        self.segunda_activity.append([tk.Button(self.segunda_activity[12][0], text="Copiar Numero de cuenta",bg=self.palette[self.buttons]),(4,1,0,0,"")])#19 BOTON INCOMPLETO
        # BOTONES
        self.segunda_activity.append([tk.Frame(self.segunda_activity[0][0],bg=self.palette[self.frames]),(3,0,0,0,"nsew")])#20
        self.botones = [("Guardar",self.guardar_f,(0,0,0,0,"")),("Cancelar",self.cancelar_f,(0,1,0,0,""))]
        for i in self.botones:# 21-22
            self.segunda_activity.append([tk.Button(self.segunda_activity[20][0], text=i[0],command=i[1],bg=self.palette[self.buttons]),i[2]])
        #TARIFA
        self.segunda_activity.append([tk.LabelFrame(self.segunda_activity[0][0], text="Orden escrita",bg=self.palette[self.labelframes]),(1,1,0,0,"nswe")])# 23
        self.segunda_activity.append([tk.Text(self.segunda_activity[23][0], height=10, width=20),(0,0,0,0,"")])# 24
        
        
        ## ESTRUCTURA DE LA PIZARRA
        ##hojas[0]
        ##    pi[0]:LB"Pedido actual"
        ##        pi[1]:L"Nombre del cliente"
        ##        pi[2]:En
        ##        pi[3]:L"Hora y fecha"
        ##        pi[4]:L"Numero del cliente"
        ##        pi[5]:En
        ##        pi[6]:L"--:--"
        ##        pi[7]:L"Direccion del cliente"
        ##        pi[8]:En
        ##        pi[9]:LF"Productos"
        ##        pi[10]:LF"costo"
        ##            pi[11]:En
        ##        pi[12]:LF"Cambio"
        ##            pi[13]:En
        ##        pi[14]:LF"Tarifa"
        ##            pi[15]:En
        ##        pi[16]:LF"Dinero para comprar"
        ##            pi[17]:En
        ##        pi[14]:LF"Metodo de pago"
        ##            pi[15]:En
        ##        pi[14]:LF"paga con ..."
        ##            pi[15]:En
        ##        pi[14]:B"Terminar orden"
        
        self.pizarra =[]
        self.pizarra.append([tk.LabelFrame(self.root,text= "Pedido Actual"),(0,0,0,0,"")])# 0
        self.pizarra.append([tk.Label(self.pizarra[0][0],text= "Nombre del cliente"),(0,0,0,0,"")])# 1
        self.pizarra.append([tk.Entry(self.pizarra[0][0],textvariable=self.main_name_cli,font=("Helvetica",15)),(0,1,0,0,"")])# 2
        self.pizarra.append([tk.Label(self.pizarra[0][0],textvariable=self.main_hora_cli),(0,2,0,0,"")])# 3
        self.pizarra.append([tk.Label(self.pizarra[0][0],text= "Numero del cliente"),(1,0,0,0,"")])# 4
        self.pizarra.append([tk.Entry(self.pizarra[0][0],textvariable=self.main_num_cli,font=("Helvetica",15)),(1,1,0,0,"")])# 5
        self.pizarra.append([tk.Label(self.pizarra[0][0],text="--:--"),(1,2,0,0,"")])# 6
        self.pizarra.append([tk.Label(self.pizarra[0][0],text= "Dirección del cliente"),(2,0,0,0,"")])# 7
        self.pizarra.append([tk.Entry(self.pizarra[0][0],textvariable=self.main_direccion_cli,font=("Helvetica",15)),(2,1,0,0,"")])# 8
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Productos"),(3,0,0,0,"")])# 9 Recuerda Cambiar
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Costo Final"),(4,0,0,0,"")])# 10
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_costo_cli,font=("Helvetica",13)),(0,0,0,0,"")])## 11
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text="Precio Final" ),(4,1,0,0,"")])# 12
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_precio_final,font=("Helvetica",15)),(0,0,0,0,"")])# 13
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Tarifa"),(5,0,0,0,"")])# 14
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_tarifa_cli,font=("Helvetica",15)),(0,0,0,0,"")])# 15
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text="Cambio" ),(5,1,0,0,"")])# 16
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_cambio_cli,font=("Helvetica",15)),(0,0,0,0,"")])# 17
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Metodo de Pago"),(6,0,0,0,"")])#18
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_metodo_pago,font=("Helvetica",15)),(0,0,0,0,"")])# 19
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.Button(self.pizarra[0][0],text="Terminar Orden",font=("Helvetica",15),command=self.terminar_orden),(7,0,0,0,"")])#20
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= " Precio Final + Tarifa"),(6,1,0,0,"")])#21
        self.pizarra.append([tk.Entry(self.pizarra[21][0],font=("Helvetica",15),textvariable=self.main_total_cli),(0,0,0,0,"")])# 22
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.iniciar_cronometro(self.pizarra[6][0], self.main_cronometro_cli)
    

           
    # OPTIMIZAR EL FLUJO DE INFORMACION
    # HACER QUE LOS DATOS YA RECABADOS EN LA PRIMERA VENTANA TERMINEN ESCRITOS EN LA SEGUNDA VENTANA Y ADEMAS SE AGREGUEN AL EXCEL
    def siguiente_f(self):
        self.orden2 = str(self.primera_activity[1][0].get("1.0", "end-1c"))# Texto extraido del Text "Analizador de texto"
        if self.orden2 == "" :
            messagebox.showwarning("Advertencia", "Falta informacion por ingresar, revise bien pendejo")
        else:
            
            
            #1 SE OBTIENE LA INFORMACION DE segunda_activity
            self.cuadernito.set(self.orden2)
            self.segunda_activity[24][0].insert(tk.END,self.orden2)
 
            #4 SE HACE LA ACTUALIZACION DE LA VENTANA BORRANDO LAS ACTIVITY 1 Y PONIENDO LA ACTIVITY 2
            self.erase(self.primera_activity)
            self.draw(self.segunda_activity,"1")
            #5 Se stablece la información en el sigueinte bloque de widgets
            
    
    def guardar_f(self):
          #     OBTENER LOS DATOS DE LOS ENTRIES Y TEXT BOX
        ###
          #
          #
        #####
        print(self.pizarra)

        self.orden2 = str(self.segunda_activity[11][0].get("1.0", "end-1c"))# Texto extraido del Text "Analizador de texto"
        metodo_pago = self.var_metodos_de_pago.get()
        if self.orden2 == "" and metodo_pago == None:
            messagebox.showwarning("Advertencia", "Falta informacion por ingresar, revise bien pendejo")
        else:
            
            #1 SE OBTIENE LA INFORMACION DE segunda_activity
            self.orden2,recoleccion = self.procesar_cadena(self.orden2)
            direccion = self.segunda_activity[3][0].get()
            nombre = self.segunda_activity[5][0].get()
            numero = self.segunda_activity[7][0].get()
            orden = self.orden2['tiendas']
            tarifa = self.orden2['pedido']['Tarifa']
            propina = self.orden2['pedido']['Propina']
                        
            #4 SE HACE LA ACTUALIZACION DE LA VENTANA BORRANDO LAS ACTIVITY 1 Y PONIENDO LA ACTIVITY 2
            self.erase(self.segunda_activity)
            self.draw(self.pizarra,"2")
            #5 Se stablece la información en el sigueinte bloque de widgets
            self.main_name_cli.set(nombre)
            self.main_num_cli.set(numero)
            self.main_direccion_cli.set(direccion)
            self.main_hora_cli.set(self.hora)
            self.main_fecha_cli.set(self.fecha)
            self.main_tarifa_cli.set(tarifa)
            self.main_metodo_pago.set(metodo_pago)
            self.tabla_precios = self.crear_widgets(self.orden2['tiendas'],self.pizarra[9][0])
            self.main_costo_cli.set(str(self.costo_total))
            self.main_precio_final.set(str(self.precio_venta))
            if metodo_pago == "Efectivo":
                paga_con =int(self.paga_con.get())
                self.main_paga_con.set(str(paga_con))
                self.main_cambio_cli.set(str(paga_con-self.precio_venta-tarifa))
            else:
                self.main_paga_con.set("Transferencia")
                self.main_cambio_cli.set("0")
            self.main_total_cli.set(str(self.precio_venta+tarifa))
            

            #3 SE ESCRIBE LA INFORMACION RECABADA PARA AÑADIRLA AL EXCEL POSTERIORMENTE

            self.list_cli = [self.fecha,#0
                        self.hora,#1
                        nombre,#2
                        numero,#3
                        recoleccion,#4
                        direccion,#5
                        orden,#6
                        self.costo_total,#7 costo total
                        self.precio_venta,#8 precio de venta
                        tarifa,#9
                        metodo_pago#10
                             ]
    def cancelar_f(self):
        self.root.destroy()

    def terminar_orden(self):
        print(self.list_cli)
        self.list_cli[6] = str(self.list_cli[6])
        self.insert_row_at_top('PEDIDITO_DB.xlsx',self.list_cli,2)
        self.root.destroy()
        
    def insert_row_at_top(self,file_path, new_row, position):
        # Abrir el archivo de Excel
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        
        # Insertar una fila al principio (en la posición 1)
        sheet.insert_rows(1)
        
        # Insertar los datos en la nueva fila
        for col_num, value in enumerate(new_row, start=1):
            sheet.cell(row=position, column=col_num, value=value)
        
        # Guardar el archivo
        workbook.save(file_path)
        
    ### METODO DE PAGO: RADIOBUTTONS COMMAND
    def metodo_pago_func(self):
        metodo = self.var_metodos_de_pago.get()# Obtener la respuesta de los radiobuttones
        self.segunda_activity[15][0].config(text=f"Pagará con:\n{metodo}")
        print(f"Metodo es : {metodo}")

        #----------------------------------------ESTO ES PARA BORRAR LOS WIDGETS RADIOBUTONS
        self.diccionarios_widgets = {"Efectivo":self.segunda_activity[13][0],"Transferencia":self.segunda_activity[14][0]}
        for i,conjunto in enumerate(self.diccionarios_widgets.values()):
            print(f"conjunto {i} es : {conjunto}")
            conjunto.grid_forget()
        if metodo == "Efectivo":
            self.segunda_activity[17][0].grid(row=self.segunda_activity[17][1][0],column=self.segunda_activity[17][1][1],padx= self.segunda_activity[17][1][2],pady = self.segunda_activity[17][1][3],sticky= self.segunda_activity[17][1][4])
        elif metodo == "Transferencia":
            self.segunda_activity[18][0].grid(row=self.segunda_activity[18][1][0],column=self.segunda_activity[18][1][1],padx= self.segunda_activity[18][1][2],pady = self.segunda_activity[18][1][3],sticky= self.segunda_activity[18][1][4])
            self.segunda_activity[19][0].grid(row=self.segunda_activity[19][1][0],column=self.segunda_activity[19][1][1],padx= self.segunda_activity[19][1][2],pady = self.segunda_activity[19][1][3],sticky= self.segunda_activity[19][1][4])

             
        
    def draw(self,activity,name):## TODO LO QUE DIBUJA A LOS WIDGETS -------------------------------------------------------------------------------------------------------------------------------
        if name == "0":
            for i,widget in enumerate(activity):            
                widget[0].grid(row=widget[1][0],column=widget[1][1],padx= widget[1][2],pady = widget[1][3],sticky= widget[1][4])
        if name == "1":
            for i,widget in enumerate(activity):
                if i == 17:# Entry de "con cuanto va a pagar el cliente
                    pass
                elif i == 18:# Texto "Numero de Tarjeta:\nXXXX-XXXX-XXXX-XXXX"
                    pass
                elif i == 19:# Texto ""
                    pass
                else:
                    widget[0].grid(row=widget[1][0],column=widget[1][1],padx= widget[1][2],pady = widget[1][3],sticky= widget[1][4])
        elif name == "2":
            for i,widget in enumerate(activity):            
                widget[0].grid(row=widget[1][0],column=widget[1][1],padx= widget[1][2],pady = widget[1][3],sticky= widget[1][4])
    def erase(self,activity):
        for i,widget in enumerate(activity):
            widget[0].grid_forget()


    def get_data(self,func):
        
        data = [self.fecha_y_hora,direccion, nombre, numero, orden]
        func(data)
        
    def borrar_texto(self,entry):
        # Borra el texto dentro del Entry al recibir un clic
        entry.delete(0, tk.END)
    # Función para restar los números y mostrar el resultado
    def restar_numeros(self,event):
        try:
            costo = float(self.main_costo_cli.get())
            pc = float(self.var_metodos_de_pago.get())
            tarifa = float(self.main_tarifa_cli.get())
            precio = float(self.main_precio_final.get())
            if pc == "Transferencia":
                self.main_cambio_cli.set("0")
            else:
                paga_con = float(self.main_paga_con.get())
                resultado = paga_con - precio - tarifa
                self.main_cambio_cli.set(resultado)
            Total = precio + tarifa
            self.main_total_cli.set(Total)
            
        except :
            # Manejar la excepción si los valores ingresados no son números
            print("finished")
##            pass

    def procesar_cadena(self,cadena):
        # Separamos la cadena en secciones utilizando los puntos como delimitadores
        secciones = cadena.split('.')
        
        # Inicializamos el diccionario que contendrá la información procesada
        resultado = {"tiendas": {}, "pedido": {}}
        recoleccion = ''
        # Procesamos las secciones de las tiendas (todas excepto la última sección)
        indice = 0
        for seccion in secciones[:-1]:# Toma la primera seccion del texto
            # Separamos la sección por comas
            partes = seccion.split(',')
           
            # El primer elemento es el nombre de la tienda
            nombre_tienda = partes[0].strip()
            recoleccion += nombre_tienda + ","
            # Inicializamos una lista para los productos de esta tienda
            productos = []
            
            # Procesamos los productos
            for producto in partes[1:]:
                textvar = tk.StringVar()
                producto = producto.strip()
                partes_producto = producto.split(' ')
                
                cantidad = float(partes_producto[0])
                nombre_producto = " ".join(partes_producto[1:-1])
                
                if '/' in partes_producto[-1]:
                    costo_compra, precio_venta = map(float, partes_producto[-1].split('/'))
                else:
                    costo_compra = precio_venta = float(partes_producto[-1])
                
                productos.append({
                    "cantidad": cantidad,
                    "nombre": nombre_producto,
                    "costo_compra": costo_compra,
                    "precio_venta": precio_venta,
                    "ID":indice
                })
                indice += 1
            
            # Guardamos la lista de productos en el diccionario de resultado
            resultado["tiendas"][nombre_tienda] = productos
        
        # Procesamos la última sección (datos del pedido)
        datos_pedido = secciones[-1].split(',')
        for dato in datos_pedido:
            clave, valor = dato.split(':')
            resultado["pedido"][clave.strip()] = float(valor.strip())
        
        return resultado, recoleccion
        
    def crear_widgets(self,tiendas, parent_widget):
        # Lista para almacenar las listas de widgets
        lista_widgets = []
        label_widget = tk.Frame(parent_widget)# Wdiget que contendra esta ventana
        label_widget.grid(row=0,column=0)# su posicion con respecto al widget padre
        contador = 0# cuenta las tiendas en las que se compro
        
        for tienda, productos in tiendas.items():
            # Label para el nombre de la tienda
            label_tienda = tk.LabelFrame(label_widget, text=f"Tienda: {tienda}")# Se crea el widget
##            lista_widgets.append([label_tienda])# Se guarda en una lista
            label_tienda.grid(row=0,column=contador)# se pone en el mapa
            contador += 1
            monto_comprado = 0
####            for i,producto in enumerate(productos):
####                # Agrega la cantidad ganada por la empresa
####                monto_comprado += producto['costo_compra']*producto['cantidad']

            for i,producto in enumerate(productos):
                # Crear los labels y el botón
                label_cantidad = tk.Label(label_tienda, text=str(producto['cantidad']))
                label_nombre = tk.Label(label_tienda, text=producto['nombre'])
                label_costo = tk.Label(label_tienda, text=str(producto['costo_compra']))
                label_precio = tk.Label(label_tienda, text=str(producto['precio_venta']))
                boton_editar = tk.Button(label_tienda, text="Editar",command=lambda o = producto:self.editar_producto(o))
                
                # Almacenar los widgets en una lista
                fila_widgets = [label_cantidad, label_nombre, label_costo, label_precio, boton_editar]
                lista_widgets.append(fila_widgets)
                self.costo_total += producto['costo_compra']*producto['cantidad']
                self.precio_venta += producto['precio_venta']*producto['cantidad']
                
                # Añadir los widgets al widget padre
                label_cantidad.grid(row=i,column=0)
                label_nombre.grid(row=i,column=1)
                label_costo.grid(row=i,column=2)
                label_precio.grid(row=i,column=3)
                boton_editar.grid(row=i,column=4)
        return lista_widgets
    
    def editar_producto(self,producto):
        
        print(producto)
        ventana_edicion = tk.Toplevel(self.root)
        ventana_edicion.title("Editar Producto")
        
        # Crear los LabelFrames y Entries
        labelframe_cantidad = tk.LabelFrame(ventana_edicion, text="Cantidad")
        labelframe_cantidad.grid(row=0, column=0,padx=4,pady=4)
        entry_cantidad = tk.Entry(labelframe_cantidad, textvariable=self.cantidad)
        entry_cantidad.grid(row=0, column=0)
##        entry_cantidad.insert(0, str(producto['cantidad']))
        
        labelframe_nombre = tk.LabelFrame(ventana_edicion, text="Nombre")
        labelframe_nombre.grid(row=0, column=1,padx=4,pady=4)
        entry_nombre = tk.Entry(labelframe_nombre,textvariable=self.nombre)
        entry_nombre.grid(row=0, column=0)
##        entry_nombre.insert(0, producto['nombre'])
        
        labelframe_costo = tk.LabelFrame(ventana_edicion, text="Costo de Compra")
        labelframe_costo.grid(row=1, column=0,padx=4,pady=4)
        entry_costo = tk.Entry(labelframe_costo,textvariable=self.costo)
        entry_costo.grid(row=0, column=0)
##        entry_costo.insert(0, str(producto['costo_compra']))
        
        labelframe_precio = tk.LabelFrame(ventana_edicion, text="Precio de Venta")
        labelframe_precio.grid(row=1, column=1,padx=4,pady=4)
        entry_precio = tk.Entry(labelframe_precio,textvariable=self.precio)
        entry_precio.grid(row=0, column=0)
##        entry_precio.insert(0, str(producto['precio_venta']))
        
        # Botón de guardar
        boton_guardar = tk.Button(ventana_edicion, text="Guardar",command=lambda o = [producto,ventana_edicion]:self.set_values(o))
        boton_guardar.grid(row=2, column=1,padx=4,pady=4)

    def set_values(self,o):
        # 1) OBTENER LOS DATOS DEL PRODUCTO
        cant = self.cantidad.get()
        nomb = self.nombre.get()
        cost = self.costo.get()
        prec = self.precio.get()
        # 2) OBTENER EL TOTAL ANTERIOR ANTES DEL CAMBIO EN PRECIO Y COSTO
        costo_anterior = float(self.main_costo_cli.get())
        precio_anterior = float(self.main_precio_final.get())
        # 3) SE ITERA A TRAVES DE LOS PRODUCTOS
        for i,fila in enumerate(self.tabla_precios):
            if o[0]["ID"] == i:
                #4) Se pone los datos obtenidos en los entries, las pone en su respectivos labels
                fila[0].config(text=cant)
                fila[1].config(text=nomb)
                fila[2].config(text=cost)
                fila[3].config(text=prec)
                # 5) Se sustituye el precio por la cantidad anterior por la nueva cantidad
                costo_nuevo = costo_anterior+float(cost)*float(cant)-float(o[0]["costo_compra"])*float(o[0]["cantidad"])
                precio_nuevo = precio_anterior+float(prec)*float(cant)-float(o[0]["precio_venta"])*float(o[0]["cantidad"])
                self.main_costo_cli.set(costo_nuevo)
                self.main_precio_final.set(precio_nuevo)
                self.main_total_cli.set(precio_nuevo+10)
                # 6) Se reestablece el precio 
                o[0]["cantidad"] = str(float(cant))
                o[0]["nombre"] = nomb
                o[0]["costo_compra"] = str(float(cost))
                o[0]["precio_venta"] = str(float(prec))
        # 7) Se 
        o[1].destroy()
         
    def iniciar_cronometro(self,etiqueta, cronometros_activos):
        print("Se inicializo el cronometro")
        cronometro = CronometroApp(etiqueta)
        cronometro.start()
        cronometros_activos.append(cronometro)

    def detener_todos_cronometros(self,cronometros_activos):
        for cronometro in cronometros_activos:
            cronometro.detener()

