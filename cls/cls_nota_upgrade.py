from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic 
from cls.cls_load_forms import table_selection 
from cls.cls_ol_table import load_list_ol
from cls.cls_database import comunication_pramso_database

class editarnota(QDialog):
    def __init__(self):
        super(editarnota, self).__init__()
        uic.loadUi("Interface/updateoderlist.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog

        self.database = comunication_pramso_database()

        #Estos line edit no pueden ser editados.
        self.idpedido_edit.setReadOnly(True)
        self.idtedit.setReadOnly(True)
        self.tractor_edit.setReadOnly(True)
        self.idcedit.setReadOnly(True)
        self.plataforma_sojera.setReadOnly(True)
        self.plataforma_maicera.setReadOnly(True)
        self.idpledit_sojero.setReadOnly(True)
        self.idpledit_maicero.setReadOnly(True)

        #<------------Botones de nueva nota------------>
        self.load_client.clicked.connect(lambda: self.loadclient())
        self.loadtractor.clicked.connect(lambda: self.cargar_tractor())
        self.loadcombine.clicked.connect(lambda: self.cargar_cosechadora())
        self.tractor_delete.clicked.connect(lambda: self.delete_tractor())
        self.combine_delete.clicked.connect(lambda: self.delete_cosechadora())
        self.loadplatform_sojero.clicked.connect(lambda: self.cargar_plataforma_sojera())
        self.loadplatform_maicero.clicked.connect(lambda: self.cargar_plataforma_maicera())
        self.sojero_delete.clicked.connect(lambda: self.delete_plataforma_sojera())
        self.maicero_delete.clicked.connect(lambda: self.delete_plataforma_maicera())
        self.borrartodo.clicked.connect(lambda: self.fun_borrartodo())
        self.guardarpedido.clicked.connect(lambda: self.fun_guardarpedido())
        self.cerrar.clicked.connect(lambda: self.close())

        #Los botones estaran en desactivados hasta que se cargue la nota de pedido del cliente
        self.loadtractor.setEnabled(False)
        self.loadcombine.setEnabled(False)
        self.loadplatform_sojero.setEnabled(False)
        self.loadplatform_maicero.setEnabled(False)

        
        
    def fun_guardarpedido(self):
        idpedido = self.idpedido_edit.text().upper()
        if idpedido != "":
            idpedido = int(self.idpedido_edit.text().upper())
            cliente = str(self.cliente_edit.text().upper())
            tractor = str(self.tractor_edit.text().upper())
            idt = str(self.idtedit.text().upper())
            cosechadora = str(self.cosechadora_edit.text().upper())
            idc = str(self.idcedit.text().upper())
            plataforma_sojera = str(self.plataforma_sojera.text().upper())
            idpl_sojera = str(self.idpledit_sojero.text().upper())
            plataforma_maicera = str(self.plataforma_maicera.text().upper())
            idpl_maicera = str(self.idpledit_maicero.text().upper())
            chasisembocador = str(self.chasisembocador.text().upper())
            observ = str(self.observaciones.text().upper())
            rodado = str(self.rodado.text().upper())
            localidad = str(self.localidad.text().upper())
            provincia = str(self.provincia.text().upper())
            fechentrega = str(self.fechentrega.text().upper())
            estado = str(self.estado.currentText())
            list_guardado = [cliente, tractor, idt, cosechadora, idc, plataforma_sojera, idpl_sojera, plataforma_maicera, idpl_maicera, chasisembocador, observ, rodado, localidad, provincia, fechentrega, estado, idpedido]
            c = 0
            for x in list_guardado:
                if x == "":
                    list_guardado[c] = "-" 
                c = c + 1

            self.database.editar_fila_ol(list_guardado)  
        
            QMessageBox.information(self, 'Guardado Correctamente', 'Cambios guardados correctamente', QMessageBox.Ok)
        else:          
            QMessageBox.warning(self, 'Error', 'No se cargo ningun pedido', QMessageBox.Ok)  
  
              

    #Borra todo el contenido de los line edit        
    def fun_borrartodo(self):
        self.idpedido_edit.setText("")
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



    def loadclient(self):
        qdialog_table = load_list_ol()
        try:
            qdialog_table.exec_()
            d = qdialog_table.list_pedido[0]
            self.idpedido_edit.setText(str(d[0]))
            self.cliente_edit.setText(d[1])
            self.tractor_edit.setText(d[3])
            self.idtedit.setText(d[4])
            self.cosechadora_edit.setText(d[5])
            self.idcedit.setText(d[6])
            self.plataforma_sojera.setText(d[7])
            self.idpledit_sojero.setText(d[8])
            self.plataforma_maicera.setText(d[9])
            self.idpledit_maicero.setText(d[10])
            self.chasisembocador.setText(d[11])
            self.observaciones.setText(d[12])
            self.rodado.setText(d[13])
            self.localidad.setText(d[14])
            self.provincia.setText(d[15])
            self.fechentrega.setText(d[16])
            #Los botones se activan
            self.loadtractor.setEnabled(True)
            self.loadcombine.setEnabled(True)
            self.loadplatform_sojero.setEnabled(True)
            self.loadplatform_maicero.setEnabled(True)
        except:
            pass

    #Carga a los line edit el equipo seleccionado del tractor
    def load_tractor(self, equip):
        self.tractor_edit.setText(str(equip[1])+" "+str(equip[2]))
        self.idtedit.setText(str(equip[0]))

    #Carga a los line edit el equipo seleccionado de la cosechadora
    def load_cosechadora(self, equip):
        self.cosechadora_edit.setText(str(equip[1])+" "+str(equip[2]))
        self.idcedit.setText(str(equip[0]))

    #Carga a los line edit el equipo seleccionado del sojero
    def load_plataforma_sojera(self, equip):
        self.plataforma_sojera.setText(str(equip[1])+" "+str(equip[2]))
        self.idpledit_sojero.setText(str(equip[0]))

    #Carga a los line edit el equipo seleccionado del maicero
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