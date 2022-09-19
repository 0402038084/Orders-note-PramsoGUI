#Interfaz Gui principal

import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QHeaderView, QMainWindow, QMessageBox

from cls.cls_database import comunication_pramso_database
from cls.cls_imprimir_nota import imprimirnota
from cls.cls_nota_actualizar import actualizarnota
from cls.cls_nota_new import nuevanota
from cls.cls_nota_upgrade import editarnota
from cls.cls_register_delete import eliminarequipo
from cls.cls_register_edit import editarequipo
from cls.cls_register_new import nuevoequipo
from cls.cls_search_ol import buscarorderlist
from cls.cls_load_prov import load_prov


class Ventanaprincipal(QMainWindow):
    def __init__(self):
        super(Ventanaprincipal, self).__init__()
        uic.loadUi('Interface/guimain.ui', self)
        self.showMaximized()

        #<------------Table configuration------------>
        self.tabla_pedidos.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)#La tabla no se edita
        self.tabla_tractor_control.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tabla_cosechadora_control.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tabla_plataforma_control.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


        #<------------Botones de menú------------>
        self.btnnota.clicked.connect(lambda: self.contenedor_pages.setCurrentWidget(self.page_nota))#Muestra el Frame Nota de pedidos
        self.btnregistro.clicked.connect(lambda: self.contenedor_pages.setCurrentWidget(self.page_registros))#Muestra el Frame Equipos
        self.btnmedidas.clicked.connect(lambda: self.contenedor_pages.setCurrentWidget(self.page_medidas)) #Muestra el Frame medidas
        self.btnee.clicked.connect(lambda: self.contenedor_pages.setCurrentWidget(self.page_ee)) #Muestra el Frame medidas
        self.btnpedidop.clicked.connect(lambda: self.contenedor_pages.setCurrentWidget(self.page_pedidop)) #Muestra el Frame medidas


        #<------------Botones de Nota de pedidos------------>
        self.refrescar_pedidos.clicked.connect(lambda: tabla_nota_pedidos())
        self.nuevopedido_pedidos.clicked.connect(lambda: nuevo_pedido_nota())
        self.buscar_ol.clicked.connect(lambda: buscar_nota_pedido())
        self.editarpedido_pedidos.clicked.connect(lambda: editar_pedido_nota())
        self.actualizarpedido_pedidos.clicked.connect(lambda: actualizar_pedido_nota())
        self.imprimirpedido_pedidos.clicked.connect(lambda: imprimir_nota())

        #<------------Metodos de los botones que se presentan en nota de pedidos------------>
        
        def buscar_nota_pedido():
            self.buscarOl = buscarorderlist()
            self.buscarOl.exec_()
            try:
                cliente = self.buscarOl.cliente
                tractor = self.buscarOl.tractor
                cosechadora = self.buscarOl.cosechadora
                plataforma_sojero = self.buscarOl.plataforma_sojero
                plataforma_maicero = self.buscarOl.plataforma_maicero
                chasisembocador = self.buscarOl.chasisembocador_
                observaciones = self.buscarOl.observaciones_
                rodado = self.buscarOl.rodado_
                localidad = self.buscarOl.localidad_
                provincia = self.buscarOl.provincia_
                estado = self.buscarOl.estado_
                if estado == "TODOS":
                    estado = ""
                datos = self.database.search_ol(cliente, tractor, cosechadora, plataforma_sojero, plataforma_maicero, chasisembocador, observaciones, rodado, localidad, provincia, estado)
                tabla_nota_pedidos_busqueda(datos)
            except:
                pass

                 
        def nuevo_pedido_nota():
            self.neworder = nuevanota()
            self.neworder.exec_()
            tabla_nota_pedidos()


        def editar_pedido_nota():
            self.updateorder = editarnota()
            self.updateorder.exec_()
            tabla_nota_pedidos()


        def actualizar_pedido_nota():
            self.actualizarorder = actualizarnota()
            self.actualizarorder.exec_()
            tabla_nota_pedidos()

        def imprimir_nota():
            self.imprimirnota = imprimirnota()
            self.imprimirnota.exec_()
            tabla_nota_pedidos()
 
                
        #<------------Cargar tabla de pedidos------------>
        def tabla_nota_pedidos():
            datos = self.database.mostrar_order_note() #Trae el metodo de la base de datos 
            i = len(datos) #Lee las filas
            self.tabla_pedidos.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_pedidos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))#ID
                self.tabla_pedidos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))#cliente
                self.tabla_pedidos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))#fecha
                self.tabla_pedidos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))#tractor
                self.tabla_pedidos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))#cosechadora
                self.tabla_pedidos.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[7]))#plataformasojera
                self.tabla_pedidos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[9]))#plataforma maicera
                self.tabla_pedidos.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_pedidos.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_pedidos.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_pedidos.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_pedidos.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_pedidos.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_pedidos.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[17]))

                for x in range(14):
                    Estado =  str(row[17])
                    if Estado == "NUEVO":
                        self.tabla_pedidos.item(tablerow, x).setBackground(QtGui.QColor(170, 255, 127))
                    elif Estado == "NORMAL": 
                        self.tabla_pedidos.item(tablerow, x).setBackground(QtGui.QColor(255, 255, 127))
                    elif Estado == "URGENTE": 
                        self.tabla_pedidos.item(tablerow, x).setBackground(QtGui.QColor(255, 99, 88))


                tablerow +=1




        #<------------Cargar tabla de pedidos con busqueda------------>
        def tabla_nota_pedidos_busqueda(datos):
            i = len(datos) #Lee las filas
            self.tabla_pedidos.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_pedidos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabla_pedidos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tabla_pedidos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tabla_pedidos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.tabla_pedidos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                self.tabla_pedidos.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[7]))
                self.tabla_pedidos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[9]))
                self.tabla_pedidos.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_pedidos.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_pedidos.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_pedidos.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_pedidos.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_pedidos.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_pedidos.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[17]))

                for x in range(14):
                    Estado =  str(row[17])
                    if Estado == "NUEVO":
                        self.tabla_pedidos.item(tablerow, x).setBackground(QtGui.QColor(170, 255, 127))
                    elif Estado == "NORMAL": 
                        self.tabla_pedidos.item(tablerow, x).setBackground(QtGui.QColor(255, 255, 127))
                    elif Estado == "URGENTE": 
                        self.tabla_pedidos.item(tablerow, x).setBackground(QtGui.QColor(255, 99, 88))
                
                tablerow +=1



        #<------------Botones de registro------------>
        self.btnrefrescar_control.clicked.connect(lambda: refrescartrabla()) #Boton refrecar tabla de control de entrega
        self.combobox_control.currentIndexChanged.connect(lambda: refrescartrabla())
        self.btnbusqueda_control.clicked.connect(lambda: search_of())#Boton busqueda de control de entrega
        self.nuevoequipo_registro.clicked.connect(lambda: fun_nuevoequipo()) #Boton para ejecutar la clase
        self.editarequipo_registro.clicked.connect(lambda: fun_editarequipo()) #Boton para ejecutar la clase
        self.eliminarequipo_registro.clicked.connect(lambda: fun_eliminarequipo()) #Boton para ejecutar la clase


        #<------------Metodos de los botones que se presentan en el registro------------>
        def fun_nuevoequipo():
            select_machine = self.combobox_control.currentText()#Variable donde tendra la pagina seleccionada
            self.newequipment = nuevoequipo() #Se carga la clase nuevo equipo
            self.newequipment.pag_actual(select_machine)#Funcion de la selección de pagina
            self.newequipment.exec_()
            refrescartrabla()

        def fun_editarequipo():
            select_machine = self.combobox_control.currentText()#Variable donde tendra la pagina seleccionada
            self.editequipment = editarequipo() #Se carga la clase editar equipo
            self.editequipment.pag_actual(select_machine)#Funcion de la selección de pagina
            self.editequipment.exec_()
            refrescartrabla()
        
        def fun_eliminarequipo():
            select_machine = self.combobox_control.currentText()#Variable donde tendra la pagina seleccionada
            self.deleteequipment = eliminarequipo() #Se carga la clase eliminar equipo
            self.deleteequipment.pag_actual(select_machine)#Funcion de la selección de pagina
            if select_machine == "Tractor":
                registers = self.database.mostrar_table_delete(select_machine) #Registro donde se guardan la consulta de la base de datos
                self.deleteequipment.table_tractor_delete(registers)#Envia la consulta de tractor
            elif select_machine == "Cosechadora":
                registers = self.database.mostrar_table_delete(select_machine) #Registro donde se guardan la consulta de la base de datos
                self.deleteequipment.table_cosechadora_delete(registers)#Envia la consulta de cosechadora
            elif select_machine == "Plataforma":
                registers = self.database.mostrar_table_delete(select_machine) #Registro donde se guardan la consulta de la base de datos
                self.deleteequipment.table_plataforma_delete(registers)#Envia la consulta de plataforma

            self.deleteequipment.exec_()


        #<------------Metodos de la tabla que se presenta en el registro------------>
        self.database = comunication_pramso_database() #Conexion a la base de datos de tractores


        def refrescartrabla():
            select_machine = self.combobox_control.currentText()#Variable donde tendra la pagina seleccionado
            if select_machine == "Tractor":
                self.tablas_control.setCurrentWidget(self.page_control_tractor) #Se mostrara pagina tractor
                mostrar_tipos_tractor()
                try:
                    self.modeloingresasdo_control.clear()#Se borrara el line edit
                except:
                    pass
            elif select_machine == "Cosechadora":
                self.tablas_control.setCurrentWidget(self.page_control_cosechadora) #Se mostrara pagina cosechadora
                mostrar_tipos_cosechadora()
                try:
                    self.modeloingresasdo_control.clear()#Se borrara el line edit
                except:
                    pass
            elif select_machine == "Plataforma":
                self.tablas_control.setCurrentWidget(self.page_control_plataforma)#Se mostrara pagina cosechadora
                mostrar_tipos_plataforma()
                try:
                    self.modeloingresasdo_control.clear()#Se borrara el line edit
                except:
                    pass


        #Para el boton buscar, se necesita comprobar que tipo de maquina esta seleccionada
        def search_of():
            select_machine = self.combobox_control.currentText()
            if select_machine == "Tractor":
                mostrar_tractor_busqueda()
            elif select_machine == "Cosechadora":
                mostrar_cosechadora_busqueda()
            elif select_machine == "Plataforma":
                mostrar_plataforma_busqueda()
                


        #Cargar la tabla de tractores
        def mostrar_tipos_tractor():
            datos = self.database.mostrar_tractor_register() #Trae el metodo de la base de datos de cosechadoras
            i = len(datos) #Lee las filas
            self.tabla_tractor_control.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_tractor_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.tabla_tractor_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tabla_tractor_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tabla_tractor_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabla_tractor_control.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                self.tabla_tractor_control.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
                self.tabla_tractor_control.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                self.tabla_tractor_control.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                self.tabla_tractor_control.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                self.tabla_tractor_control.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
                self.tabla_tractor_control.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_tractor_control.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_tractor_control.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_tractor_control.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_tractor_control.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_tractor_control.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_tractor_control.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
                self.tabla_tractor_control.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
                self.tabla_tractor_control.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
                self.tabla_tractor_control.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))
                self.tabla_tractor_control.setItem(tablerow,20,QtWidgets.QTableWidgetItem(row[21]))
                self.tabla_tractor_control.setItem(tablerow,21,QtWidgets.QTableWidgetItem(row[22]))
                self.tabla_tractor_control.setItem(tablerow,22,QtWidgets.QTableWidgetItem(row[23]))
                self.tabla_tractor_control.setItem(tablerow,23,QtWidgets.QTableWidgetItem(row[24]))
                self.tabla_tractor_control.setItem(tablerow,24,QtWidgets.QTableWidgetItem(row[25]))
                self.tabla_tractor_control.setItem(tablerow,25,QtWidgets.QTableWidgetItem(row[26]))
                self.tabla_tractor_control.setItem(tablerow,26,QtWidgets.QTableWidgetItem(row[27]))
                self.tabla_tractor_control.setItem(tablerow,27,QtWidgets.QTableWidgetItem(row[28]))


                tablerow +=1
                
        mostrar_tipos_tractor()


        #Cargar la tabla de cosechadoras
        def mostrar_tipos_cosechadora():
            datos = self.database.mostrar_cosechadora_register() #Trae el metodo de la base de datos 
            i = len(datos) #Lee las filas
            self.tabla_cosechadora_control.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_cosechadora_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.tabla_cosechadora_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tabla_cosechadora_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tabla_cosechadora_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabla_cosechadora_control.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                self.tabla_cosechadora_control.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
                self.tabla_cosechadora_control.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                self.tabla_cosechadora_control.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                self.tabla_cosechadora_control.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                self.tabla_cosechadora_control.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
                self.tabla_cosechadora_control.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_cosechadora_control.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_cosechadora_control.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_cosechadora_control.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_cosechadora_control.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_cosechadora_control.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_cosechadora_control.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
                self.tabla_cosechadora_control.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
                self.tabla_cosechadora_control.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
                self.tabla_cosechadora_control.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))

                tablerow +=1



        #Cargar la tabla de plataformas
        def mostrar_tipos_plataforma():
            datos = self.database.mostrar_plataforma_register() #Trae el metodo de la base de datos 
            i = len(datos) #Lee las filas
            self.tabla_plataforma_control.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_plataforma_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.tabla_plataforma_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tabla_plataforma_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tabla_plataforma_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.tabla_plataforma_control.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
                self.tabla_plataforma_control.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
                self.tabla_plataforma_control.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                self.tabla_plataforma_control.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                self.tabla_plataforma_control.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                self.tabla_plataforma_control.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
                self.tabla_plataforma_control.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_plataforma_control.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_plataforma_control.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_plataforma_control.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_plataforma_control.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_plataforma_control.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_plataforma_control.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))


                tablerow +=1


        #<------------Metodos de busqueda para mostrar en la tabla------------>
        #Cargar la tabla con busqueda de modelo de tractor
        def mostrar_tractor_busqueda():
            Modelo = self.modeloingresasdo_control.text().upper()
            Modelo = str(Modelo)
            if Modelo != "":
                datos = self.database.buscar_tractor_register(Modelo) #Trae el metodo de la base de datos
                
                i = len(datos) #Lee las filas
                self.tabla_tractor_control.setRowCount(i) #Ejecuta la cantodad de filas
                tablerow = 0  #Variable contable para posicionarse en una fila
                for row in datos:
                    self.tabla_tractor_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tabla_tractor_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tabla_tractor_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tabla_tractor_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tabla_tractor_control.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                    self.tabla_tractor_control.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
                    self.tabla_tractor_control.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                    self.tabla_tractor_control.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                    self.tabla_tractor_control.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                    self.tabla_tractor_control.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
                    self.tabla_tractor_control.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
                    self.tabla_tractor_control.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
                    self.tabla_tractor_control.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
                    self.tabla_tractor_control.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
                    self.tabla_tractor_control.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
                    self.tabla_tractor_control.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
                    self.tabla_tractor_control.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
                    self.tabla_tractor_control.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
                    self.tabla_tractor_control.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
                    self.tabla_tractor_control.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))
                    self.tabla_tractor_control.setItem(tablerow,20,QtWidgets.QTableWidgetItem(row[21]))
                    self.tabla_tractor_control.setItem(tablerow,21,QtWidgets.QTableWidgetItem(row[22]))
                    self.tabla_tractor_control.setItem(tablerow,22,QtWidgets.QTableWidgetItem(row[23]))
                    self.tabla_tractor_control.setItem(tablerow,23,QtWidgets.QTableWidgetItem(row[24]))
                    self.tabla_tractor_control.setItem(tablerow,24,QtWidgets.QTableWidgetItem(row[25]))
                    self.tabla_tractor_control.setItem(tablerow,25,QtWidgets.QTableWidgetItem(row[26]))
                    self.tabla_tractor_control.setItem(tablerow,26,QtWidgets.QTableWidgetItem(row[27]))
                    self.tabla_tractor_control.setItem(tablerow,27,QtWidgets.QTableWidgetItem(row[28]))
                    
                    tablerow +=1
            else:
                pass


        #Cargar la tabla con busqueda de modelo de cosechadora
        def mostrar_cosechadora_busqueda():
            Modelo = self.modeloingresasdo_control.text().upper()
            Modelo = str(Modelo)
            if Modelo != "":
                datos = self.database.buscar_cosechadora_register(Modelo) #Trae el metodo de la base de datos
                i = len(datos) #Lee las filas
                self.tabla_cosechadora_control.setRowCount(i) #Ejecuta la cantodad de filas
                tablerow = 0  #Variable contable para posicionarse en una fila
                for row in datos:
                    self.tabla_cosechadora_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tabla_cosechadora_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tabla_cosechadora_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tabla_cosechadora_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tabla_cosechadora_control.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                    self.tabla_cosechadora_control.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
                    self.tabla_cosechadora_control.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                    self.tabla_cosechadora_control.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                    self.tabla_cosechadora_control.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                    self.tabla_cosechadora_control.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
                    self.tabla_cosechadora_control.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
                    self.tabla_cosechadora_control.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
                    self.tabla_cosechadora_control.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
                    self.tabla_cosechadora_control.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
                    self.tabla_cosechadora_control.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
                    self.tabla_cosechadora_control.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
                    self.tabla_cosechadora_control.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
                    self.tabla_cosechadora_control.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
                    self.tabla_cosechadora_control.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
                    self.tabla_cosechadora_control.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))


                    tablerow +=1
            else:
                pass


        #Cargar la tabla con busqueda de modelo de plataforma
        def mostrar_plataforma_busqueda():
            Modelo = self.modeloingresasdo_control.text().upper()
            Modelo = str(Modelo)
            if Modelo != "":
                datos = self.database.buscar_plataforma_register(Modelo) #Trae el metodo de la base de datos
                i = len(datos) #Lee las filas
                self.tabla_plataforma_control.setRowCount(i) #Ejecuta la cantodad de filas
                tablerow = 0  #Variable contable para posicionarse en una fila
                for row in datos:
                    self.tabla_plataforma_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tabla_plataforma_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tabla_plataforma_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tabla_plataforma_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                    self.tabla_plataforma_control.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tabla_plataforma_control.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
                    self.tabla_plataforma_control.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                    self.tabla_plataforma_control.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                    self.tabla_plataforma_control.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                    self.tabla_plataforma_control.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
                    self.tabla_plataforma_control.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
                    self.tabla_plataforma_control.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
                    self.tabla_plataforma_control.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
                    self.tabla_plataforma_control.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
                    self.tabla_plataforma_control.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
                    self.tabla_plataforma_control.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
                    self.tabla_plataforma_control.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))


                    tablerow +=1
            else:
                pass

        tabla_nota_pedidos()


        #EQUIPOS ENTREGADOS

        self.refrescar_ee.clicked.connect(lambda: tabla_ee())
        self.restaurar_ee.clicked.connect(lambda: restaurar_ol())
        self.tabla_pedidos_entregados.cellClicked.connect(lambda: habilitar_botones())
        self.restaurar_ee.setEnabled(False)
        self.borrar_ee.setEnabled(False)
        self.buscar_ol_ee.clicked.connect(lambda: buscar_ee())
        self.borrar_ee.clicked.connect(lambda: borrar_ee())

        def buscar_ee():
            self.buscarOl = buscarorderlist()
            self.buscarOl.exec_()
            try:
                cliente = self.buscarOl.cliente
                tractor = self.buscarOl.tractor
                cosechadora = self.buscarOl.cosechadora
                plataforma_sojero = self.buscarOl.plataforma_sojero
                plataforma_maicero = self.buscarOl.plataforma_maicero
                chasisembocador = self.buscarOl.chasisembocador_
                observaciones = self.buscarOl.observaciones_
                rodado = self.buscarOl.rodado_
                localidad = self.buscarOl.localidad_
                provincia = self.buscarOl.provincia_
                estado = self.buscarOl.estado_
                if estado == "TODOS":
                    estado = ""
                datos = self.database.search_ol_ee(cliente, tractor, cosechadora, plataforma_sojero, plataforma_maicero, chasisembocador, observaciones, rodado, localidad, provincia, estado)
                tabla_ee_busqueda(datos)
            except:
                pass



        def tabla_ee():
            datos = self.database.mostrar_ee() #Trae el metodo de la base de datos 
            i = len(datos) #Lee las filas
            self.tabla_pedidos_entregados.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_pedidos_entregados.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))#ID
                self.tabla_pedidos_entregados.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))#cliente
                self.tabla_pedidos_entregados.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))#fecha
                self.tabla_pedidos_entregados.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))#tractor
                self.tabla_pedidos_entregados.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))#cosechadora
                self.tabla_pedidos_entregados.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[7]))#plataformasojera
                self.tabla_pedidos_entregados.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[9]))#plataforma maicera
                self.tabla_pedidos_entregados.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_pedidos_entregados.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_pedidos_entregados.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_pedidos_entregados.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_pedidos_entregados.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_pedidos_entregados.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_pedidos_entregados.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[17]))

                tablerow +=1
                
        tabla_ee()
        
        #<------------Cargar tabla de pedidos con busqueda------------>
        def tabla_ee_busqueda(datos):
            i = len(datos) #Lee las filas
            self.tabla_pedidos_entregados.setRowCount(i) #Ejecuta la cantidad de filas
            tablerow = 0  #Variable contable para posicionarse en una fila
            for row in datos:
                self.tabla_pedidos_entregados.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabla_pedidos_entregados.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tabla_pedidos_entregados.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tabla_pedidos_entregados.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.tabla_pedidos_entregados.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                self.tabla_pedidos_entregados.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[7]))
                self.tabla_pedidos_entregados.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[9]))
                self.tabla_pedidos_entregados.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[11]))
                self.tabla_pedidos_entregados.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[12]))
                self.tabla_pedidos_entregados.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[13]))
                self.tabla_pedidos_entregados.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[14]))
                self.tabla_pedidos_entregados.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[15]))
                self.tabla_pedidos_entregados.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[16]))
                self.tabla_pedidos_entregados.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[17]))

                for x in range(14):
                    Estado =  str(row[17])
                    if Estado == "NUEVO":
                        self.tabla_pedidos_entregados.item(tablerow, x).setBackground(QtGui.QColor(170, 255, 127))
                    elif Estado == "NORMAL": 
                        self.tabla_pedidos_entregados.item(tablerow, x).setBackground(QtGui.QColor(255, 255, 127))
                    elif Estado == "URGENTE": 
                        self.tabla_pedidos_entregados.item(tablerow, x).setBackground(QtGui.QColor(255, 99, 88))
                
                tablerow +=1

                                
        def habilitar_botones():
            self.restaurar_ee.setEnabled(True)
            self.borrar_ee.setEnabled(True)

        def deshabilitar_botones():
            self.restaurar_ee.setEnabled(False)
            self.borrar_ee.setEnabled(False)
            
        def restaurar_ol():
            try:
                row = self.tabla_pedidos_entregados.currentItem().row() #Indica la fila del item seleccionado.
            except:
                row = ""
                
            if row != "":
                result = QMessageBox.question(self, 'Restaurar', '¿Estas seguro de que quieres restaurar este equipo entregado?', QMessageBox.Ok|QMessageBox.Cancel)
                
                if result == QMessageBox.Ok: 
                    row = self.tabla_pedidos_entregados.currentItem().row() #Indica la fila del item seleccionado.
                    id = self.pedido = self.tabla_pedidos_entregados.item(row,0).text() #Selecciona un item segun las coordenadas. De la fila
                    pedido = int(id)
                    datos_DB = self.database.search_id_backup(pedido)
                    datos = datos_DB[0]
                    self.database.Restaurar_equipo_entregado(datos)
                    self.database.eliminar_fila_ee(pedido)
                    tabla_ee()
                    tabla_nota_pedidos()
                    deshabilitar_botones()
                else:
                    pass
            else:
                QMessageBox.warning(self, 'Error', 'No seleccionaste ningun pedido', QMessageBox.Ok)
                
        def borrar_ee():
            try:
                row = self.tabla_pedidos_entregados.currentItem().row() #Indica la fila del item seleccionado.
            except:
                row = ""
        
            if row != "":
                result = QMessageBox.question(self, 'Eliminar', '¿Estas seguro de que quieres eliminar este equipo entregado?', QMessageBox.Ok|QMessageBox.Cancel)
                
                if result == QMessageBox.Ok: 
                    row = self.tabla_pedidos_entregados.currentItem().row() #Indica la fila del item seleccionado.
                    id = self.pedido = self.tabla_pedidos_entregados.item(row,0).text() #Selecciona un item segun las coordenadas. De la fila
                    pedido = int(id)
                    self.database.eliminar_fila_ee(pedido)
                    tabla_ee()
                    tabla_nota_pedidos()
                    deshabilitar_botones()
                else:
                    pass
            else:
                QMessageBox.warning(self, 'Error', 'No seleccionaste ningun pedido', QMessageBox.Ok)
                
            
        #<------------Tabla de pedido a proveedor------------>
        
        self.cargarproveedor.clicked.connect(lambda: cargar_proveedor())#Muestra el Frame Nota de pedidos

        
        def cargar_n_pedido():
            db = self.database.id_pp()
            db_select = db[0]
            numero = int(db_select[0]) + 1  
            self.n_prov.setText(str(numero))
            
        def cargar_proveedor():
            self.loadprov = load_prov() #Se carga la clase editar equipo
            self.loadprov.exec_()
            self.proveedor.setText(self.loadprov.list_equipment[1])
            self.id_prov.setText(str(self.loadprov.list_equipment[0]))

        cargar_n_pedido()

    

if __name__ == "__main__":
    app=QApplication(sys.argv)
    my_app=Ventanaprincipal()
    my_app.setWindowTitle('Pramso - Sistema de gestión de datos')
    my_app.show()
    sys.exit(app.exec_())
