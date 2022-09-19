from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView, QDialog
from PyQt5 import uic 
from cls.cls_database import comunication_pramso_database

class load_prov(QDialog):
    def __init__(self):
        super(load_prov, self).__init__()
        uic.loadUi("Interface/loadprov.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog
        self.database = comunication_pramso_database()
        self.cargar_tabla()
        self.tabla_provcar.cellDoubleClicked.connect(lambda: self.get_prov())

    #Cargar la tabla de tractores
    def cargar_tabla(self):
        datos = self.database.proveedores() #Trae el metodo de la base de datos de cosechadoras
        i = len(datos) #Lee las filas
        self.tabla_provcar.setRowCount(i) #Ejecuta la cantidad de filas
        tablerow = 0  #Variable contable para posicionarse en una fila
        for row in datos:
            self.tabla_provcar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabla_provcar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))

            tablerow +=1
        
    def get_prov(self):
        self.list_equipment = []
        row = self.tabla_provcar.currentItem().row()
        columncantidad = self.tabla_provcar.columnCount()

        for x in range(columncantidad):
            self.equipment = self.tabla_provcar.item(row,x).text()
            self.list_equipment.append(str(self.equipment)) 
    
        self.close()
