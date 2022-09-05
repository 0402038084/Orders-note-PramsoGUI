from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView, QDialog
from PyQt5 import uic 
from cls.cls_database import comunication_pramso_database
from cls.cls_search_ol import buscarorderlist 


class load_list_ol(QDialog):
    def __init__(self):
        super(load_list_ol, self).__init__()
        uic.loadUi("Interface/loadorderlist.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog

        self.buscar.clicked.connect(lambda: self.buscar_nota_pedido())
        self.cerrar.clicked.connect(lambda: self.close())
        self.tabla_pedidos.cellDoubleClicked.connect(lambda: self.load_lineedit_ol())

        self.database = comunication_pramso_database()
        self.tabla_nota_pedidos()

    #<------------Cargar tabla de pedidos------------>
    def tabla_nota_pedidos(self):
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
            

    def buscar_nota_pedido(self):
        self.buscarOl = buscarorderlist()
        self.buscarOl.exec_()
        try:
            cliente = self.buscarOl.cliente
            tractor = self.buscarOl.tractor
            cosechadora = self.buscarOl.cosechadora
            plataforma = self.buscarOl.plataforma
            chasisembocador = self.buscarOl.chasisembocador
            observaciones = self.buscarOl.observaciones
            rodado = self.buscarOl.rodado
            localidad = self.buscarOl.localidad
            provincia = self.buscarOl.provincia
            estado = self.buscarOl.estado
            if estado == "TODOS":
                estado = ""
                datos = self.database.search_ol(cliente, tractor, cosechadora, plataforma, chasisembocador, observaciones, rodado, localidad, provincia, estado)
                self.tabla_nota_pedidos_busqueda(datos)
        except:
            pass


    #<------------Cargar tabla de pedidos con busqueda------------>
    def tabla_nota_pedidos_busqueda(self, datos):
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


    #<------------Cargar equipo------------>
    def load_lineedit_ol(self):
        row = self.tabla_pedidos.currentItem().row() #Indica la fila del item seleccionado.
        self.pedido = self.tabla_pedidos.item(row,0).text() #Selecciona un item segun las coordenadas. De la fila
        pedido = int(self.pedido)
        self.list_pedido = self.database.search_id(pedido)
        
        self.close()