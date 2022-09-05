from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic 
from cls.cls_database import comunication_pramso_database 


class nuevoequipo(QDialog):
    def __init__(self): #Constructor de Dialog
        super(nuevoequipo, self).__init__()
        uic.loadUi("Interface/Windownewequipments.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog


        self.btnguardar_t.clicked.connect(lambda: self.correct_save_tractor()) #Boton para guardar en la base de datos
        self.borrar_t.clicked.connect(lambda: self.delete_all_tractor()) #Boton para borrar los datos de las lineas de editar
        self.reiniciar_t.clicked.connect(lambda: self.reset_all_tractor()) #Boton para reiniciar los datos de las lineas de editar        
        self.cerrar_t.clicked.connect(lambda: self.close())#Boton para cerrar ventana dialog

        self.btnguardar_c.clicked.connect(lambda: self.correct_save_cosechadora()) #Boton para guardar en la base de datos
        self.borrar_c.clicked.connect(lambda: self.delete_all_cosechadora()) #Boton para borrar los datos de las lineas de editar
        self.reiniciar_c.clicked.connect(lambda: self.reset_all_cosechadora()) #Boton para reiniciar los datos de las lineas de editar
        self.cerrar_c.clicked.connect(lambda: self.close())#Boton para cerrar ventana dialog

        self.btnguardar_pl.clicked.connect(lambda: self.correct_save_plataforma()) #Boton para guardar en la base de datos
        self.borrar_pl.clicked.connect(lambda: self.delete_all_plataforma()) #Boton para borrar los datos de las lineas de editar
        self.reiniciar_pl.clicked.connect(lambda: self.reset_all_plataforma()) #Boton para reiniciar los datos de las lineas de editar
        self.cerrar_pl.clicked.connect(lambda: self.close())#Boton para cerrar ventana dialog



    db_newequipment = comunication_pramso_database()


    #<------------Metodo para guardar en la base de datos------------>
    def correct_save_tractor(self):
        ID_T = self.ID_T.text().upper()#Toma el ID
        machinary = "tractor"
        Contenedor = self.db_newequipment.comprobar_ID(ID_T, machinary)
        if len((ID_T)) == 6:
            #Lee las demas variables del equipo
            if len(Contenedor) == 0:
                Marca = self.tractor_marca.currentText().upper()
                Modelo = self.tractor_modelo.text().upper()
                Bases = self.bases_tractor.text().upper()
                Adaptadores = self.adaptadores_tractor.text().upper()
                Cogote = self.cogote_tractor.text().upper()
                Frente = self.frente_tractor.text().upper()
                Brazos = self.brazos_tractor.text().upper()
                Placaportabrazos = self.placaportabr_tractor.text().upper()
                Portarolo = self.portarolo_tractor.text().upper()
                Rolo = self.rolo_tractor.text().upper()
                Cilindros = self.cilindros.text().upper()
                Topes = self.topes.text().upper()
                Mangueras = self.mangueras.text().upper()
                Banderas = self.banderas.text().upper()
                Riendas = self.riendas.text().upper()
                Bulones5_8 = self.bulones58_tractor.text().upper()
                Bulones7_8 = self.bulones78_tractor.text().upper()
                Bulones20mm = self.bulones20mm_tractor.text().upper()
                Bulones9_16 = self.bulones916_tractor.text().upper()
                Grampas = self.grampas_tractor.text().upper()
                Resortes = self.resortes_tractor.text().upper()
                Calcos = self.calcos_tractor.text().upper()
                Kit_hidraulico = self.kithid.text().upper()
                Kit_transferencia = self.kittran.text().upper()
                Teflon = self.teflon.text().upper()
                Precintos = self.precintos.text().upper()
                equipment_save = [ID_T, Marca, Modelo, Bases, Adaptadores, Cogote, Frente, Brazos, Placaportabrazos, Portarolo, Rolo, Cilindros, Topes, Mangueras, Banderas, Riendas, Bulones5_8, Bulones7_8, Bulones20mm, Bulones9_16, Grampas, Resortes, Calcos, Kit_hidraulico, Kit_transferencia, Teflon, Precintos]
                self.db_newequipment.new_tractor(equipment_save)
                QMessageBox.information(self, 'Guardado', 'Guardado correctamente', QMessageBox.Ok)
                self.reset_all_tractor()
            elif len(Contenedor) != 0:
                QMessageBox.critical(self, 'Error', 'Este ID ya existe', QMessageBox.Ok)
        elif len(ID_T) > 6:
            QMessageBox.critical(self, 'Error', 'Ingresaste mas de 6 caracteres', QMessageBox.Ok)
        elif len(ID_T) < 6:
            QMessageBox.critical(self, 'Error', 'Ingresaste menos de 6 caracteres', QMessageBox.Ok)



    def correct_save_cosechadora(self):
        ID_C = self.ID_C.text().upper()#Toma el ID
        machinary = "cosechadora"
        Contenedor = self.db_newequipment.comprobar_ID(ID_C, machinary)
        if len((ID_C)) == 6:
            #Lee las demas variables del equipo
            if len(Contenedor) == 0:
                Marca = self.cosechadora_marca.currentText().upper()
                Modelo = self.cosechadora_modelo.text().upper()
                Bases = self.bases_cosechadora.text().upper()
                Placaportacadena = self.placaportacade_cosechadora.text().upper()
                Grampascadena = self.grampascade_cosechadora.text().upper()
                Frente = self.frente_cosechadora.text().upper()
                Brazos = self.brazos_cosechadora.text().upper()
                Placaportabrazos = self.placaportabr_cosechadora.text().upper()
                Portarolo = self.portarolo_cosechadora.text().upper()
                Rolo = self.rolo_cosechadora.text().upper()
                Bulones5_8 = self.bulones58_cosechadora.text().upper()
                Bulones7_8 = self.bulones78_cosechadora.text().upper()
                Bulones20mm = self.bulones20mm_cosechadora.text().upper()
                Bulones9_16 = self.bulones916_cosechadora.text().upper()
                Bulones1_2 = self.bulones12_cosechadora.text().upper()
                Grampas = self.grampas_cosechadora.text().upper()
                Resortes = self.resortes_cosechadora.text().upper()
                Calcos = self.calcos_cosechadora.text().upper()
                equipment_save = [ID_C, Marca, Modelo, Bases, Placaportacadena, Grampascadena, Frente, Brazos, Placaportabrazos, Portarolo, Rolo, Bulones5_8, Bulones7_8, Bulones20mm, Bulones9_16, Bulones1_2, Grampas, Resortes, Calcos,]
                self.db_newequipment.new_cosechadora(equipment_save)
                QMessageBox.information(self, 'Guardado', 'Guardado correctamente', QMessageBox.Ok)
                self.reset_all_cosechadora()
            elif len(Contenedor) != 0:
                QMessageBox.critical(self, 'Error', 'Este ID ya existe', QMessageBox.Ok)
        elif len(ID_C) > 6:
            QMessageBox.critical(self, 'Error', 'Ingresaste mas de 6 caracteres', QMessageBox.Ok)
        elif len(ID_C) < 6:
            QMessageBox.critical(self, 'Error', 'Ingresaste menos de 6 caracteres', QMessageBox.Ok)




    def correct_save_plataforma(self):
        ID_PL= self.ID_PL.text().upper()#Toma el ID
        machinary = "plataforma"
        Contenedor = self.db_newequipment.comprobar_ID(ID_PL, machinary)
        if len((ID_PL)) == 6:
            #Lee las demas variables del equipo
            if len(Contenedor) == 0:
                Marca = self.plataforma_marca.currentText().upper()
                Modelo = self.plataforma_modelo.text().upper()
                Tipodepl = self.tipopl.currentText().upper()
                Bases = self.bases_pl.text().upper()
                Brazos = self.brazos_pl.text().upper()
                Portarolo = self.portarolo_pl.text().upper()
                Rolo = self.rolo_pl.text().upper()
                Bulones5_8 = self.bulones58_pl.text().upper()
                Bulones1_2 = self.bulones12_pl.text().upper()
                Bulones20mm = self.bulones20mm_pl.text().upper()
                Bulones9_16 = self.bulones916_pl.text().upper()
                Grampas = self.grampas_pl.text().upper()
                Resortes = self.resortes_pl.text().upper()
                Calcos = self.calcos_pl.text().upper()
                Adaptador = self.adaptador_pl.text().upper()
                equipment_save = [ID_PL, Marca, Modelo, Tipodepl, Bases, Brazos, Portarolo, Rolo, Bulones5_8, Bulones20mm, Bulones9_16, Bulones1_2, Grampas, Resortes, Calcos, Adaptador]
                self.db_newequipment.new_plataforma(equipment_save)
                QMessageBox.information(self, 'Guardado', 'Guardado correctamente', QMessageBox.Ok)
                self.reset_all_plataforma()
            elif len(Contenedor) != 0:
                QMessageBox.critical(self, 'Error', 'Este ID ya existe', QMessageBox.Ok) 
        elif len(ID_PL) > 6:
            QMessageBox.critical(self, 'Error', 'Ingresaste mas de 6 caracteres', QMessageBox.Ok)
        elif len(ID_PL) < 6:
            QMessageBox.critical(self, 'Error', 'Ingresaste menos de 6 caracteres', QMessageBox.Ok)






    #<------------Metodo para borrar todos los line edit------------>

    ###################### TRACTOR ######################
    def delete_all_tractor(self):
        self.ID_T.setText("")
        self.tractor_modelo.setText("")
        self.bases_tractor.setText("")
        self.adaptadores_tractor.setText("")
        self.cogote_tractor.setText("")
        self.frente_tractor.setText("")
        self.brazos_tractor.setText("")
        self.placaportabr_tractor.setText("")
        self.portarolo_tractor.setText("")
        self.rolo_tractor.setText("")
        self.cilindros.setText("")
        self.topes.setText("")
        self.mangueras.setText("")
        self.banderas.setText("")
        self.riendas.setText("")
        self.bulones58_tractor.setText("")
        self.bulones78_tractor.setText("")
        self.bulones20mm_tractor.setText("")
        self.bulones916_tractor.setText("")
        self.grampas_tractor.setText("")
        self.resortes_tractor.setText("")
        self.calcos_tractor.setText("")
        self.kithid.setText("")
        self.kittran.setText("")
        self.teflon.setText("")
        self.precintos.setText("")


    ###################### COSECHADORA ######################
    def delete_all_cosechadora(self):
        self.ID_C.setText("")
        self.cosechadora_modelo.setText("")
        self.bases_cosechadora.setText("")
        self.placaportacade_cosechadora.setText("")
        self.grampascade_cosechadora.setText("")
        self.frente_cosechadora.setText("")
        self.brazos_cosechadora.setText("")
        self.placaportabr_cosechadora.setText("")
        self.portarolo_cosechadora.setText("")
        self.rolo_cosechadora.setText("")
        self.bulones58_cosechadora.setText("")
        self.bulones78_cosechadora.setText("")
        self.bulones20mm_cosechadora.setText("")
        self.bulones916_cosechadora.setText("")
        self.bulones12_cosechadora.setText("")
        self.grampas_cosechadora.setText("")
        self.resortes_cosechadora.setText("")
        self.calcos_cosechadora.setText("")


    ###################### PLATAFORMA ######################
    def delete_all_plataforma(self):
        self.ID_PL.setText("")
        self.plataforma_modelo.setText("")
        self.bases_pl.setText("")
        self.brazos_pl.setText("")
        self.portarolo_pl.setText("")
        self.rolo_pl.setText("")
        self.bulones58_pl.setText("")
        self.bulones12_pl.setText("")
        self.bulones20mm_pl.setText("")
        self.bulones916_pl.setText("")
        self.grampas_pl.setText("")
        self.resortes_pl.setText("")
        self.calcos_pl.setText("")
        self.adaptador_pl.setText("")

    

    #<------------Metodos para reiniciar todos los line edit------------>

    ###################### TRACTOR ######################
    def reset_all_tractor(self):
        self.ID_T.setText("")
        self.tractor_modelo.setText("")
        self.bases_tractor.setText("2")
        self.adaptadores_tractor.setText("-")
        self.cogote_tractor.setText("2")
        self.frente_tractor.setText("3")
        self.brazos_tractor.setText("4")
        self.placaportabr_tractor.setText("4")
        self.portarolo_tractor.setText("2")
        self.rolo_tractor.setText("2")
        self.cilindros.setText("2")
        self.topes.setText("-")
        self.mangueras.setText("2")
        self.banderas.setText("2")
        self.riendas.setText("-")
        self.bulones58_tractor.setText("-")
        self.bulones78_tractor.setText("6")
        self.bulones20mm_tractor.setText("-")
        self.bulones916_tractor.setText("-")
        self.grampas_tractor.setText("12+8")
        self.resortes_tractor.setText("4")
        self.calcos_tractor.setText("OK")
        self.kithid.setText("2")
        self.kittran.setText("2")
        self.teflon.setText("1")
        self.precintos.setText("25")


    ###################### COSECHADORA ######################
    def reset_all_cosechadora(self):
        self.ID_C.setText("")
        self.cosechadora_modelo.setText("")
        self.bases_cosechadora.setText("2")
        self.placaportacade_cosechadora.setText("-")
        self.grampascade_cosechadora.setText("2")
        self.frente_cosechadora.setText("3")
        self.brazos_cosechadora.setText("4")
        self.placaportabr_cosechadora.setText("4")
        self.portarolo_cosechadora.setText("2")
        self.rolo_cosechadora.setText("2")
        self.bulones58_cosechadora.setText("-")
        self.bulones78_cosechadora.setText("-")
        self.bulones20mm_cosechadora.setText("-")
        self.bulones916_cosechadora.setText("-")
        self.bulones12_cosechadora.setText("-")
        self.grampas_cosechadora.setText("12+8")
        self.resortes_cosechadora.setText("4")
        self.calcos_cosechadora.setText("OK")
        

    ###################### PLATAFORMA ######################
    def reset_all_plataforma(self):
        self.ID_PL.setText("")
        self.plataforma_modelo.setText("")
        self.bases_pl.setText("4")
        self.brazos_pl.setText("4")
        self.portarolo_pl.setText("2")
        self.rolo_pl.setText("2")
        self.bulones58_pl.setText("-")
        self.bulones12_pl.setText("-")
        self.bulones20mm_pl.setText("-")
        self.bulones916_pl.setText("-")
        self.grampas_pl.setText("-")
        self.resortes_pl.setText("4")
        self.calcos_pl.setText("OK")
        self.adaptador_pl.setText("-")

            


    def pag_actual(self, select_machine):
            if select_machine == "Tractor":
                self.new_pages.setCurrentWidget(self.page_tractor)
            elif select_machine == "Cosechadora":
                self.new_pages.setCurrentWidget(self.page_cosechadora)
            elif select_machine == "Plataforma":
                self.new_pages.setCurrentWidget(self.page_plataforma)
            else:
                pass
