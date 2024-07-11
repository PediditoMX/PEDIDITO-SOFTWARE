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



class Iniciar_sesion:
        
    def __init__(self,root):
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
        self.usuario = tk.StringVar() # Recoje la primer orden escrita 
        self.contrasena = tk.StringVar()# 5
        
#    #                                                                                      
#   # #                #        #                 #        #        #                       
#  #   #     #####    ###             #    #              ###               #####    #####  
# #     #   #          #       ##     #    #     ##        #       ##      #    #   #       
# #######   #          #        #     #    #      #        #        #      #####     #####  
# #     #   #          #        #      #  #       #        #        #      #             #  
# #     #    #####      ##    #####     ##      #####       ##    #####     #####   #####   

        ## VENTANA
        self.root = root
##        self.root.geometry()

        ##      ESTRUCTURA DE LA VENTANA
        
        self.primera_activity = []
        self.primera_activity.append([tk.Frame(self.root,bg=dusk[4]),(0,0,50,50,"nsew")])# 0
        self.primera_activity.append([tk.Label(self.primera_activity[0][0], text="Ingrese al Sistema\nPEDIDITO SOFTWARE"),(0,0,10,10,"nsew")])# 1
        self.primera_activity.append([tk.Button(self.primera_activity[0][0],text=">",font=("Helvetica",20),fg=dusk[1],bg=dusk[3],command=self.terminar_orden),(3,0,0,(20,0),"")])#10
        self.primera_activity.append([tk.Entry(self.primera_activity[0][0],textvariable=self.usuario,font=("Helvetica",20),fg=dusk[2],bg=dusk[4] ),(1,0,0,20,"")])#10
        self.primera_activity.append([tk.Entry(self.primera_activity[0][0],textvariable=self.contrasena,font=("Helvetica",20),fg=dusk[1],bg=dusk[4] ),(2,0,0,20,"")])#10

        
        self.draw(self.primera_activity,"0")
        self.usuario.set("Usuario")
        self.contrasena.set("Contrasena")
    def terminar_orden(self):
##        print(self.list_cli)
##        self.list_cli[6] = str(self.list_cli[6])
##        self.insert_row_at_top('PEDIDITO_DB.xlsx',self.list_cli,2)
        self.root.destroy()
        
           
        
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

         
    def iniciar_cronometro(self,etiqueta, cronometros_activos):
        print("Se inicializo el cronometro")
        cronometro = CronometroApp(etiqueta)
        cronometro.start()
        cronometros_activos.append(cronometro)

    def detener_todos_cronometros(self,cronometros_activos):
        for cronometro in cronometros_activos:
            cronometro.detener()

