from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic 
from cls.cls_load_forms import table_selection
from cls.cls_database import comunication_pramso_database


class eliminarequipo(QDialog):
    def __init__(self):
        super(eliminarequipo, self).__init__()
        uic.loadUi("Interface/Windowdeleteequipments.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog
        self.tabla_tractor_control.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)#La tabla no se edita
        self.tabla_cosechadora_control.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)#La tabla no se edita
        self.tabla_plataforma_control.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)#La tabla no se edita
        self.textEdit.setReadOnly(True)
        self.textEdit_c.setReadOnly(True)
        self.textEdit_p.setReadOnly(True)
        self.buscar_t.clicked.connect(lambda: self.load_search_tractor())
        self.buscar_c.clicked.connect(lambda: self.load_search_cosechadora())
        self.buscar_pl.clicked.connect(lambda: self.load_search_cosechadora())
        
        self.eliminar_t.clicked.connect(lambda: self.eliminar_tractor())
        self.eliminar_c.clicked.connect(lambda: self.eliminar_cosechadora())
        self.eliminar_pl.clicked.connect(lambda: self.eliminar_plataforma())



    database = comunication_pramso_database()

    def pag_actual(self, select_machine):
            if select_machine == "Tractor":
                self.delete_pages.setCurrentWidget(self.page_tractor)
            elif select_machine == "Cosechadora":
                self.delete_pages.setCurrentWidget(self.page_cosechadora)
            elif select_machine == "Plataforma":
                self.delete_pages.setCurrentWidget(self.page_plataforma)
            else:
                pass
            
            
 #<------------Cargar equipo------------>
    def load_lineedit_tractor(self):
        self.list_equipment = []
        row = self.tabla_tractor_control.currentItem().row()
        columncantidad = self.tabla_tractor_control.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_tractor_control.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
        

    def load_lineedit_cosechadora(self):
        self.list_equipment = []
        row = self.tabla_cosechadora.currentItem().row()
        columncantidad = self.tabla_cosechadora_control.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_cosechadora_control.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
        

    def load_lineedit_plataforma(self):
        self.list_equipment = []
        row = self.tabla_plataforma_control.currentItem().row()
        columncantidad = self.tabla_plataforma.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_plataforma_control.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
        

    #<------------tablas de ventana delete------------>

    #carga la tabla delete tractor
    def table_tractor_delete(self, registers):

        i = len(registers) #lee las filas
        self.tabla_tractor_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in registers:
            self.tabla_tractor_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_tractor_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_tractor_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            
            tablerow +=1

    #carga la tabla delete cosechadora
    def table_cosechadora_delete(self, registers):

        i = len(registers) #lee las filas
        self.tabla_cosechadora_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in registers:
            self.tabla_cosechadora_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_cosechadora_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_cosechadora_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            
            tablerow +=1


    #carga la tabla delete plataforma
    def table_plataforma_delete(self, registers):

        i = len(registers) #lee las filas
        self.tabla_plataforma_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in registers:
            self.tabla_plataforma_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_plataforma_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            
            tablerow +=1
            

    #<------------tablas de ventana busqueda delete------------>
    def load_search_tractor(self):
        ID = self.id_t.text().upper()
        MARCA = str(self.marca_t.currentText().upper())
        MODELO = self.modelo_t.text().upper()
        if MARCA == "SELECCIONAR":
            MARCA = ""
        datos = self.database.load_tabletractor_upgrade(ID, MARCA, MODELO) #Trae el metodo de la base de datos de cosechadoras
        i = len(datos) #Lee las filas
        self.tabla_tractor_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_tractor_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_tractor_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_tractor_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1
            
            
    def load_search_cosechadora(self):
        ID = self.id_c.text().upper()
        MARCA = str(self.marca_c.currentText().upper())
        MODELO = self.modelo_c.text().upper()
        if MARCA == "SELECCIONAR":
            MARCA = ""
        datos = self.database.load_tablecosechadora_upgrade(ID, MARCA, MODELO) #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_cosechadora_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_cosechadora_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_cosechadora_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_cosechadora_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            tablerow +=1


    def load_search_plataforma(self):
        ID = self.id_pl.text().upper()
        MARCA = str(self.marca_pl.currentText().upper()) 
        MODELO = self.modelo_pl.text().upper()    
        TIPOPLATAFORMA = str(self.tipoplataforma_pl.currentText().upper()) 
        if MARCA == "SELECCIONAR":
            MARCA = ""
        if TIPOPLATAFORMA == "SELECCIONAR":
            TIPOPLATAFORMA = ""
        datos = self.database.load_tableplataforma(ID, MARCA, MODELO, TIPOPLATAFORMA) #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_plataforma_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_plataforma_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))  
            self.tabla_plataforma_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3])) 
            tablerow +=1
                     
                     
            #carga la tabla delete tractor
    def table_tractor(self):
        registers = self.database.mostrar_table_delete("Tractor") #Registro donde se guardan la consulta de la base de datos
        i = len(registers) #lee las filas
        self.tabla_tractor_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in registers:
            self.tabla_tractor_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_tractor_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_tractor_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            
            tablerow +=1

    #carga la tabla delete cosechadora
    def table_cosechadora(self):
        registers = self.database.mostrar_table_delete("Cosechadora") #Registro donde se guardan la consulta de la base de datos
        i = len(registers) #lee las filas
        self.tabla_cosechadora_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in registers:
            self.tabla_cosechadora_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_cosechadora_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_cosechadora_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            
            tablerow +=1
    
    
        #carga la tabla delete plataforma
    def table_plataforma(self):
        registers = self.database.mostrar_table_delete("Plataforma") #Registro donde se guardan la consulta de la base de datos
        i = len(registers) #lee las filas
        self.tabla_plataforma_control.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in registers:
            self.tabla_plataforma_control.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma_control.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma_control.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_plataforma_control.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            
            tablerow +=1
                     
    def eliminar_tractor(self):
        try:
            row = self.tabla_tractor_control.currentItem().row() #Indica la fila del item seleccionado.
        except:
            row = ""
        
        if row != "":    
            self.pedido = self.tabla_tractor_control.item(row,0).text() #Selecciona un item segun las coordenadas. De la fila
            pedido = str(self.pedido)
            msg = QMessageBox.warning(self, 'Eliminar', '¿Esta seguro de eliminar este equipo?', QMessageBox.Ok|QMessageBox.Cancel)
            if msg == QMessageBox.Ok:
                self.database.eliminar_fila_tractor(pedido)
                self.table_tractor()
            else:
                pass
        else:
            msg = QMessageBox.information(self, 'Error', 'No seleccionaste ningun equipo', QMessageBox.Ok)


    def eliminar_cosechadora(self):
        try:
            row = self.tabla_cosechadora_control.currentItem().row() #Indica la fila del item seleccionado.
        except:
            row = ""
        
        if row != "":    
            self.pedido = self.tabla_cosechadora_control.item(row,0).text() #Selecciona un item segun las coordenadas. De la fila
            pedido = str(self.pedido)
            msg = QMessageBox.warning(self, 'Eliminar', '¿Esta seguro de eliminar este equipo?', QMessageBox.Ok|QMessageBox.Cancel)
            if msg == QMessageBox.Ok:
                self.database.eliminar_fila_cosechadora(pedido)
                self.table_cosechadora()
            else:
                pass
        else:
            msg = QMessageBox.information(self, 'Error', 'No seleccionaste ningun equipo', QMessageBox.Ok)
 
        
    def eliminar_plataforma(self):
        try:
            row = self.tabla_plataforma_control.currentItem().row() #Indica la fila del item seleccionado.
        except:
            row = ""
        
        if row != "":    
            self.pedido = self.tabla_plataforma_control.item(row,0).text() #Selecciona un item segun las coordenadas. De la fila
            pedido = str(self.pedido)
            msg = QMessageBox.warning(self, 'Eliminar', '¿Esta seguro de eliminar este equipo?', QMessageBox.Ok|QMessageBox.Cancel)
            if msg == QMessageBox.Ok:
                self.database.eliminar_fila_plataforma(pedido)
                self.table_plataforma()
            else:
                pass
        else:
            msg = QMessageBox.information(self, 'Error', 'No seleccionaste ningun equipo', QMessageBox.Ok)
 
