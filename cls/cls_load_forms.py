import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView, QDialog
from PyQt5 import uic 
from cls.cls_database import comunication_pramso_database


class table_selection(QDialog):
    def __init__(self):
        super(table_selection, self).__init__()
        uic.loadUi("Interface/Tableupgrade.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog
        
        #<------------Table configuration------------>
        self.tabla_tractor.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tabla_cosechadora.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tabla_plataforma.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #Conexión a base de datos
        self.database = comunication_pramso_database()
        
        self.buscar_t.clicked.connect(lambda: self.load_search_tractor())
        self.buscar_c.clicked.connect(lambda: self.load_search_cosechadora())
        self.buscar_pl.clicked.connect(lambda: self.load_search_plataforma())

        self.tabla_tractor.cellDoubleClicked.connect(lambda: self.load_lineedit_tractor())
        self.tabla_cosechadora.cellDoubleClicked.connect(lambda: self.load_lineedit_cosechadora())
        self.tabla_plataforma.cellDoubleClicked.connect(lambda: self.load_lineedit_plataforma())

    
    #<------------Cargar pestaña y titulo------------>
    def window_tittle_table(self, machine):
        if machine == "Tractor":
            self.titulosuperior.setText("TRACTOR") #cambio de titulo
            self.pagesoftables.setCurrentWidget(self.page_t)
            self.mostrar_tipos_tractor()
        elif machine == "Cosechadora":
            self.titulosuperior.setText("COSECHADORA")#cambio de titulo
            self.pagesoftables.setCurrentWidget(self.page_c)
            self.mostrar_tipos_cosechadora()
        elif machine == "Plataforma":
            self.titulosuperior.setText("PLATAFORMA")#cambio de titulo
            self.pagesoftables.setCurrentWidget(self.page_pl)
            self.mostrar_tipos_plataforma()
        elif machine == "Sojero":
            self.titulosuperior.setText("PLATAFORMA SOJERA")#cambio de titulo
            self.pagesoftables.setCurrentWidget(self.page_pl)
            self.mostrar_tipos_sojeros()
        elif machine == "Maicero":
            self.titulosuperior.setText("PLATAFORMA MAICERA")#cambio de titulo
            self.pagesoftables.setCurrentWidget(self.page_pl)
            self.mostrar_tipos_maiceros()
        


        
    
    #<------------Metodos para cargar DATABASE en la tabla------------>

    #Cargar la tabla de tractores
    def mostrar_tipos_tractor(self):
        datos = self.database.mostrar_tractor_register() #Trae el metodo de la base de datos de cosechadoras
        i = len(datos) #Lee las filas
        self.tabla_tractor.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_tractor.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_tractor.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_tractor.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_tractor.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_tractor.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.tabla_tractor.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_tractor.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_tractor.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_tractor.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_tractor.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_tractor.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_tractor.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_tractor.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_tractor.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_tractor.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_tractor.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_tractor.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
            self.tabla_tractor.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
            self.tabla_tractor.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
            self.tabla_tractor.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))
            self.tabla_tractor.setItem(tablerow,20,QtWidgets.QTableWidgetItem(row[21]))
            self.tabla_tractor.setItem(tablerow,21,QtWidgets.QTableWidgetItem(row[22]))
            self.tabla_tractor.setItem(tablerow,22,QtWidgets.QTableWidgetItem(row[23]))
            self.tabla_tractor.setItem(tablerow,23,QtWidgets.QTableWidgetItem(row[24]))
            self.tabla_tractor.setItem(tablerow,24,QtWidgets.QTableWidgetItem(row[25]))
            self.tabla_tractor.setItem(tablerow,25,QtWidgets.QTableWidgetItem(row[26]))
            self.tabla_tractor.setItem(tablerow,26,QtWidgets.QTableWidgetItem(row[27]))
            self.tabla_tractor.setItem(tablerow,27,QtWidgets.QTableWidgetItem(row[28]))


            tablerow +=1


    #Cargar la tabla de cosechadoras
    def mostrar_tipos_cosechadora(self):
        datos = self.database.mostrar_cosechadora_register() #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_cosechadora.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_cosechadora.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_cosechadora.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_cosechadora.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_cosechadora.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_cosechadora.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.tabla_cosechadora.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_cosechadora.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_cosechadora.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_cosechadora.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_cosechadora.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_cosechadora.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_cosechadora.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_cosechadora.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_cosechadora.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_cosechadora.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_cosechadora.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_cosechadora.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
            self.tabla_cosechadora.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
            self.tabla_cosechadora.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
            self.tabla_cosechadora.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))

            tablerow +=1



    #Cargar la tabla de plataformas
    def mostrar_tipos_plataforma(self):
        datos = self.database.mostrar_plataforma_register() #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_plataforma.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_plataforma.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_plataforma.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_plataforma.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_plataforma.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_plataforma.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_plataforma.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_plataforma.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_plataforma.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_plataforma.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_plataforma.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_plataforma.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_plataforma.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_plataforma.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_plataforma.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_plataforma.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))           
            
            tablerow +=1



    #Cargar la tabla de plataformas sojeras
    def mostrar_tipos_sojeros(self):
        datos = self.database.mostrar_plataforma_sojera() #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_plataforma.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_plataforma.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_plataforma.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_plataforma.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_plataforma.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_plataforma.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_plataforma.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_plataforma.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_plataforma.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_plataforma.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_plataforma.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_plataforma.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_plataforma.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_plataforma.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_plataforma.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_plataforma.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))           
            
            tablerow +=1



    #Cargar la tabla de plataformas maiceros
    def mostrar_tipos_maiceros(self):
        datos = self.database.mostrar_plataforma_maicera() #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_plataforma.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_plataforma.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_plataforma.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_plataforma.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_plataforma.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_plataforma.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_plataforma.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_plataforma.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_plataforma.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_plataforma.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_plataforma.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_plataforma.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_plataforma.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_plataforma.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_plataforma.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_plataforma.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))           
            
            tablerow +=1

    #<------------Metodos para cargar consulta de DATABASE en la tabla------------>

    def load_search_tractor(self):
        ID = self.id_t.text().upper()
        MARCA = self.marca_t.text().upper()
        MODELO = self.modelo_t.text().upper()
        datos = self.database.load_tabletractor_upgrade(ID, MARCA, MODELO) #Trae el metodo de la base de datos de cosechadoras
        i = len(datos) #Lee las filas
        self.tabla_tractor.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_tractor.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_tractor.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_tractor.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_tractor.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_tractor.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.tabla_tractor.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_tractor.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_tractor.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_tractor.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_tractor.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_tractor.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_tractor.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_tractor.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_tractor.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_tractor.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_tractor.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_tractor.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
            self.tabla_tractor.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
            self.tabla_tractor.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
            self.tabla_tractor.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))
            self.tabla_tractor.setItem(tablerow,20,QtWidgets.QTableWidgetItem(row[21]))
            self.tabla_tractor.setItem(tablerow,21,QtWidgets.QTableWidgetItem(row[22]))
            self.tabla_tractor.setItem(tablerow,22,QtWidgets.QTableWidgetItem(row[23]))
            self.tabla_tractor.setItem(tablerow,23,QtWidgets.QTableWidgetItem(row[24]))
            self.tabla_tractor.setItem(tablerow,24,QtWidgets.QTableWidgetItem(row[25]))
            self.tabla_tractor.setItem(tablerow,25,QtWidgets.QTableWidgetItem(row[26]))
            self.tabla_tractor.setItem(tablerow,26,QtWidgets.QTableWidgetItem(row[27]))
            self.tabla_tractor.setItem(tablerow,27,QtWidgets.QTableWidgetItem(row[28]))


            tablerow +=1

    def load_search_cosechadora(self):
        ID = self.id_c.text().upper()
        MARCA = self.marca_c.text().upper()
        MODELO = self.modelo_c.text().upper()
        datos = self.database.load_tablecosechadora_upgrade(ID, MARCA, MODELO) #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_cosechadora.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_cosechadora.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_cosechadora.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_cosechadora.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_cosechadora.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.tabla_cosechadora.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.tabla_cosechadora.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_cosechadora.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_cosechadora.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_cosechadora.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_cosechadora.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_cosechadora.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_cosechadora.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_cosechadora.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_cosechadora.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_cosechadora.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_cosechadora.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_cosechadora.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))
            self.tabla_cosechadora.setItem(tablerow,17,QtWidgets.QTableWidgetItem(row[18]))
            self.tabla_cosechadora.setItem(tablerow,18,QtWidgets.QTableWidgetItem(row[19]))
            self.tabla_cosechadora.setItem(tablerow,19,QtWidgets.QTableWidgetItem(row[20]))

            tablerow +=1

    def load_search_plataforma(self):
        ID = self.id_pl.text().upper()
        MARCA = self.marca_pl.text().upper()
        MODELO = self.modelo_pl.text().upper()        
        datos = self.database.load_tableplataforma_upgrade(ID, MARCA, MODELO) #Trae el metodo de la base de datos 
        i = len(datos) #Lee las filas
        self.tabla_plataforma.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_plataforma.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_plataforma.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_plataforma.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_plataforma.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_plataforma.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_plataforma.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_plataforma.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_plataforma.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tabla_plataforma.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.tabla_plataforma.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.tabla_plataforma.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[11]))
            self.tabla_plataforma.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[12]))
            self.tabla_plataforma.setItem(tablerow,12,QtWidgets.QTableWidgetItem(row[13]))
            self.tabla_plataforma.setItem(tablerow,13,QtWidgets.QTableWidgetItem(row[14]))
            self.tabla_plataforma.setItem(tablerow,14,QtWidgets.QTableWidgetItem(row[15]))
            self.tabla_plataforma.setItem(tablerow,15,QtWidgets.QTableWidgetItem(row[16]))
            self.tabla_plataforma.setItem(tablerow,16,QtWidgets.QTableWidgetItem(row[17]))           
            
            tablerow +=1

    #<------------Cargar equipo------------>
    def load_lineedit_tractor(self):
        #variable = self.tabla_plataforma.selectedItems(2)
        self.list_equipment = []
        row = self.tabla_tractor.currentItem().row()
        columncantidad = self.tabla_tractor.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_tractor.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
        
        self.close()

    def load_lineedit_cosechadora(self):
        #variable = self.tabla_plataforma.selectedItems(2)
        self.list_equipment = []
        row = self.tabla_cosechadora.currentItem().row()
        columncantidad = self.tabla_cosechadora.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_cosechadora.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
        
        self.close()


    def load_lineedit_plataforma(self):
        #variable = self.tabla_plataforma.selectedItems(2)
        self.list_equipment = []
        row = self.tabla_plataforma.currentItem().row()
        columncantidad = self.tabla_plataforma.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_plataforma.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
        
        self.close()