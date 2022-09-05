from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic 
from cls.cls_load_forms import table_selection 
from cls.cls_database import comunication_pramso_database
import datetime

class nuevanota(QDialog):
    def __init__(self):
        super(nuevanota, self).__init__()
        uic.loadUi("Interface/neworderlist.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog

        self.database = comunication_pramso_database()

        #Estos line edit no pueden ser editados.
        self.idtedit.setReadOnly(True)
        self.tractor_edit.setReadOnly(True)
        self.idcedit.setReadOnly(True)
        self.plataforma_sojera.setReadOnly(True)
        self.plataforma_maicera.setReadOnly(True)
        self.idpledit_sojero.setReadOnly(True)
        self.idpledit_maicero.setReadOnly(True)


        #<------------Botones de nueva nota------------>
        self.loadtractor.clicked.connect(lambda: self.cargar_tractor())
        self.loadcombine.clicked.connect(lambda: self.cargar_cosechadora())
        self.tractor_delete.clicked.connect(lambda: self.delete_tractor())
        self.combine_delete.clicked.connect(lambda: self.delete_cosechadora())
        self.loadplatform_sojero.clicked.connect(lambda: self.cargar_plataforma_sojera())
        self.loadplatform_maicero.clicked.connect(lambda: self.cargar_plataforma_maicera())
        self.sojero_delete.clicked.connect(lambda: self.delete_plataforma_sojera())
        self.maicero_delete.clicked.connect(lambda: self.delete_plataforma_maicera())
        self.borrartodo.clicked.connect(lambda: self.fun_borrartodo())
        self.guardarpedido.clicked.connect(lambda: self.fun_guardar())
        self.cerrar.clicked.connect(lambda: self.close())


    #Guarda todos los datos ingresados en los lineedit en la base de datos
    def fun_guardar(self):
        cliente = str(self.cliente_edit.text().upper())
        if cliente != "":
            f = datetime.datetime.now()
            cliente = str(self.cliente_edit.text().upper())
            fecha = str(str(f.day)+"/"+str(f.month)+"/"+str(f.year))
            tractor = str(self.tractor_edit.text().upper())
            idt = str(self.idtedit.text().upper())
            cosechadora = str(self.cosechadora_edit.text().upper())
            idc = str(self.idcedit.text().upper())
            plataforma_sojera = str(self.plataforma_sojera.text().upper())
            idpl_sojera = str(self.idpledit_sojero.text().upper())
            plataforma_maicero = str(self.plataforma_maicera.text().upper())
            idpl_maicero = str(self.idpledit_maicero.text().upper())
            chasisembocador = str(self.chasisembocador.text().upper())
            observ = str(self.observaciones.text().upper())
            rodado = str(self.rodado.text().upper())
            localidad = str(self.localidad.text().upper())
            provincia = str(self.provincia.text().upper())
            fechentrega = str(self.fechentrega.text().upper())
            estado = str(self.estado.currentText())
            list_guardado = [cliente, fecha, tractor, idt, cosechadora, idc, plataforma_sojera, idpl_sojera, plataforma_maicero, idpl_maicero, chasisembocador, observ, rodado, localidad, provincia, fechentrega, estado]
            c = 0
            for x in list_guardado:
                if x == "":
                    list_guardado[c] = "-" 
                c = c + 1

            self.database.guardar_nueva_fila_ol(list_guardado)
            QMessageBox.information(self, 'Guardado', 'Guardado correctamente', QMessageBox.Ok)
            self.close()
        else: 
            QMessageBox.warning(self, 'Error', 'No se ingreso ningun nombre de cliente al pedido', QMessageBox.Ok)




    #Borra todo el contenido de los line edit        
    def fun_borrartodo(self):
        self.cliente_edit.setText("")
        self.tractor_edit.setText("")
        self.idtedit.setText("")
        self.cosechadora_edit.setText("")
        self.idcedit.setText("")
        self.plataforma_sojera.setText("")
        self.idpledit_sojero.setText("")
        self.plataforma_maicera.setText("")
        self.idpledit_maicero.setText("")
        self.chasisembocador.setText("")
        self.observaciones.setText("")
        self.rodado.setText("")
        self.localidad.setText("")
        self.provincia.setText("")
        self.fechentrega.setText("")


    
    #Carga tabla de tractores
    def cargar_tractor(self):
        machine = "Tractor"
        self.tableselection = table_selection()
        self.tableselection.window_tittle_table(machine)
        self.tableselection.exec_()
        try:
            equipment_selected = self.tableselection.list_equipment
            self.load_tractor(equipment_selected)
        except:
            pass


    #Carga tabla de cosechadoras
    def cargar_cosechadora(self):
        machine = "Cosechadora"
        self.tableselection = table_selection()
        self.tableselection.window_tittle_table(machine)
        self.tableselection.exec_()
        try:
            equipment_selected = self.tableselection.list_equipment
            self.load_cosechadora(equipment_selected)
        except:
            pass


    #Carga tabla de plataforma
    def cargar_plataforma_sojera(self):
        machine = "Sojero"
        self.tableselection = table_selection()
        self.tableselection.window_tittle_table(machine)
        self.tableselection.exec_()  
        try:
            equipment_selected = self.tableselection.list_equipment
            self.load_plataforma_sojera(equipment_selected)    
        except:
            pass


    #Carga tabla de plataforma
    def cargar_plataforma_maicera(self):
        machine = "Maicero"
        self.tableselection = table_selection()
        self.tableselection.window_tittle_table(machine)
        self.tableselection.exec_()  
        try:
            equipment_selected = self.tableselection.list_equipment
            self.load_plataforma_maicera(equipment_selected)    
        except:
            pass




    #Carga a los line edit el equipo seleccionado del tractor
    def load_tractor(self, equip):
        self.tractor_edit.setText(str(equip[1])+" "+str(equip[2]))
        self.idtedit.setText(str(equip[0]))


    #Carga a los line edit el equipo seleccionado del tractor
    def load_cosechadora(self, equip):
        self.cosechadora_edit.setText(str(equip[1])+" "+str(equip[2]))
        self.idcedit.setText(str(equip[0]))


    #Carga a los line edit el equipo seleccionado del tractor
    def load_plataforma_sojera(self, equip):
        self.plataforma_sojera.setText(str(equip[1])+" "+str(equip[2]))
        self.idpledit_sojero.setText(str(equip[0]))


    #Carga a los line edit el equipo seleccionado del tractor
    def load_plataforma_maicera(self, equip):
        self.plataforma_maicera.setText(str(equip[1])+" "+str(equip[2]))
        self.idpledit_maicero.setText(str(equip[0]))




    #elimina line edit el equipo seleccionado del tractor
    def delete_tractor(self):
        self.tractor_edit.setText("")
        self.idtedit.setText("")

    #elimina line edit el equipo seleccionado de la cosechadora
    def delete_cosechadora(self):
        self.cosechadora_edit.setText("")
        self.idcedit.setText("")

    #elimina line edit el equipo seleccionado del sojero
    def delete_plataforma_sojera(self):
        self.plataforma_sojera.setText("")
        self.idpledit_sojero.setText("")

    #elimina line edit el equipo seleccionado del maicero
    def delete_plataforma_maicera(self):
        self.plataforma_maicera.setText("")
        self.idpledit_maicero.setText("")



