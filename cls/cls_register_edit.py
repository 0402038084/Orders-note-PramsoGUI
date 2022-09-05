from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic 
from cls.cls_load_forms import table_selection 
from cls.cls_database import comunication_pramso_database


class editarequipo(QDialog):
    def __init__(self):
        super(editarequipo, self).__init__()
        uic.loadUi("Interface/Windoweditequipments.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog
        self.tractor_marca.setReadOnly(True)
        self.cosechadora_marca.setReadOnly(True)
        self.plataforma_marca.setReadOnly(True)
        self.tractor_modelo.setReadOnly(True)
        self.cosechadora_modelo.setReadOnly(True)
        self.plataforma_modelo.setReadOnly(True)
        self.ID_T.setReadOnly(True)
        self.ID_C.setReadOnly(True)
        self.ID_PL.setReadOnly(True)


        self.btncargar_t.clicked.connect(lambda: self.cargar_tractor()) #Boton para cargar tabla de seleccion
        self.btnguardar_t.clicked.connect(lambda: self.correct_upgrade_tractor()) #Boton para guardar en la base de datos
        self.borrar_t.clicked.connect(lambda: self.delete_all_tractor()) #Boton para borrar los datos de las lineas de editar
        self.reiniciar_t.clicked.connect(lambda: self.reset_all_tractor()) #Boton para reiniciar los datos de las lineas de editar        
        self.cerrar_t.clicked.connect(lambda: self.close())#Boton para cerrar ventana dialog

        self.btncargar_c.clicked.connect(lambda: self.cargar_cosechadora()) #Boton para cargar tabla de seleccion
        self.btnguardar_c.clicked.connect(lambda: self.correct_upgrade_cosechadora()) #Boton para guardar en la base de datos
        self.borrar_c.clicked.connect(lambda: self.delete_all_cosechadora()) #Boton para borrar los datos de las lineas de editar
        self.reiniciar_c.clicked.connect(lambda: self.reset_all_cosechadora()) #Boton para reiniciar los datos de las lineas de editar
        self.cerrar_c.clicked.connect(lambda: self.close())#Boton para cerrar ventana dialog

        self.btncargar_pl.clicked.connect(lambda: self.cargar_plataforma()) #Boton para cargar tabla de seleccion
        self.btnguardar_pl.clicked.connect(lambda: self.correct_upgrade_plataforma()) #Boton para guardar en la base de datos
        self.borrar_pl.clicked.connect(lambda: self.delete_all_plataforma()) #Boton para borrar los datos de las lineas de editar
        self.reiniciar_pl.clicked.connect(lambda: self.reset_all_plataforma()) #Boton para reiniciar los datos de las lineas de editar
        self.cerrar_pl.clicked.connect(lambda: self.close())#Boton para cerrar ventana dialog

        self.db = comunication_pramso_database()
        
 #<------------Metodo para guardar en la base de datos------------>
    def correct_upgrade_tractor(self):
        IDT = str(self.ID_T.text().upper())
        modelo = str(self.tractor_modelo.text().upper())
        bases = str(self.bases_tractor.text().upper())
        adaptadores = str(self.adaptadores_tractor.text().upper())
        cogote = str(self.cogote_tractor.text().upper())
        frente = str(self.frente_tractor.text().upper())
        brazos = str(self.brazos_tractor.text().upper())
        placaportabr = str(self.placaportabr_tractor.text().upper())
        portarolo = str(self.portarolo_tractor.text().upper())
        rolo = str(self.rolo_tractor.text().upper())
        cilindros = str(self.cilindros.text().upper())
        topes = str(self.topes.text().upper())
        mangueras = str(self.mangueras.text().upper())
        banderas = str(self.banderas.text().upper())
        riendas = str(self.riendas.text().upper())
        bulones58 = str(self.bulones58_tractor.text().upper())
        bulones78 = str(self.bulones78_tractor.text().upper())
        bulones20 = str(self.bulones20mm_tractor.text().upper())
        bulones916 = str(self.bulones916_tractor.text().upper())
        grampas = str(self.grampas_tractor.text().upper())
        resortes = str(self.resortes_tractor.text().upper())
        calcos = str(self.calcos_tractor.text().upper())
        kithid = str(self.kithid.text().upper())
        kittran = str(self.kittran.text().upper())
        teflon = str(self.teflon.text().upper())
        precintos = str(self.precintos.text().upper())
        equipment_save = [IDT, modelo, bases, adaptadores, cogote, frente, brazos, placaportabr, portarolo, rolo, cilindros, topes, mangueras, banderas, riendas, bulones58, bulones78, bulones20, bulones916, grampas, resortes, calcos, kithid, kittran, teflon, precintos]
        self.db.edit_tractor(equipment_save)
        QMessageBox.information(self, 'Guardado', 'Editado correctamente', QMessageBox.Ok)
        self.reset_all_tractor()
        
        
    def correct_upgrade_cosechadora(self):
        IDC = str(self.ID_C.text().upper())
        modelo = str(self.cosechadora_modelo.text().upper())
        bases = str(self.bases_cosechadora.text().upper())
        placaportacade = str(self.placaportacade_cosechadora.text().upper())
        grampascade = str(self.grampascade_cosechadora.text().upper())
        frente = str(self.frente_cosechadora.text().upper())
        brazos = str(self.brazos_cosechadora.text().upper())
        placaportabr = str(self.placaportabr_cosechadora.text().upper())
        portarolo = str(self.portarolo_cosechadora.text().upper())
        rolo = str(self.rolo_cosechadora.text().upper())
        bulones58 = str(self.bulones58_cosechadora.text().upper())
        bulones78 = str(self.bulones78_cosechadora.text().upper())
        bulones20 = str(self.bulones20mm_cosechadora.text().upper())
        bulones916 = str(self.bulones916_cosechadora.text().upper())
        bulones12 = str(self.bulones12_cosechadora.text().upper())
        grampas = str(self.grampas_cosechadora.text().upper())
        resortes = str(self.resortes_cosechadora.text().upper())
        calcos = str(self.calcos_cosechadora.text().upper())
        equipment_save = [IDC, modelo, bases, placaportacade, grampascade, frente, brazos, placaportabr, portarolo, rolo, bulones58, bulones78, bulones20, bulones916, bulones12, grampas, resortes, calcos]
        self.db.edit_cosechadora(equipment_save)
        QMessageBox.information(self, 'Guardado', 'Editado correctamente', QMessageBox.Ok)
        self.reset_all_cosechadora()
        
    def correct_upgrade_plataforma(self):
        IDPL = str(self.ID_PL.text().upper())
        modelo = str(self.plataforma_modelo.text().upper())
        tipodeplataforma = str(self.tipoplataforma.currentText().upper())
        bases = str(self.bases_pl.text().upper())
        brazos = str(self.brazos_pl.text().upper())
        portarolo = str(self.portarolo_pl.text().upper())
        rolo = str(self.rolo_pl.text().upper())
        bulones58 = str(self.bulones58_pl.text().upper())
        bulones12 = str(self.bulones12_pl.text().upper())
        bulones20 = str(self.bulones20mm_pl.text().upper())
        bulones916 = str(self.bulones916_pl.text().upper())
        grampas = str(self.grampas_pl.text().upper())
        resortes = str(self.resortes_pl.text().upper())
        calcos = str(self.calcos_pl.text().upper())
        adaptadores = str(self.adaptadores_pl.text().upper())
        equipment_save = [IDPL, modelo, tipodeplataforma, bases, brazos, portarolo, rolo, bulones58, bulones12, bulones20, bulones916, grampas, resortes, calcos, adaptadores]
        self.db.edit_plataforma(equipment_save)
        QMessageBox.information(self, 'Guardado', 'Editado correctamente', QMessageBox.Ok)
        self.reset_all_plataforma()
 #<------------Metodo para cargar equipos------------>

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

    def cargar_plataforma(self):
        machine = "Plataforma"
        self.tableselection = table_selection()
        self.tableselection.window_tittle_table(machine)
        self.tableselection.exec_()     
        try:
            equipment_selected = self.tableselection.list_equipment
            self.load_plataforma(equipment_selected)   
        except:
            pass

    #<------------Metodos para cargar los line edit------------>
    def load_tractor(self, equip):

        self.ID_T.setText(equip[0])
        self.tractor_marca.setText(equip[1])
        self.tractor_modelo.setText(equip[2])
        self.bases_tractor.setText(equip[4])
        self.adaptadores_tractor.setText(equip[5])
        self.cogote_tractor.setText(equip[6])
        self.frente_tractor.setText(equip[7])
        self.brazos_tractor.setText(equip[8])
        self.placaportabr_tractor.setText(equip[9])
        self.portarolo_tractor.setText(equip[10])
        self.rolo_tractor.setText(equip[11])
        self.cilindros.setText(equip[12])
        self.topes.setText(equip[13])
        self.mangueras.setText(equip[14])
        self.banderas.setText(equip[15])
        self.riendas.setText(equip[16])
        self.bulones58_tractor.setText(equip[17])
        self.bulones78_tractor.setText(equip[18])
        self.bulones20mm_tractor.setText(equip[19])
        self.bulones916_tractor.setText(equip[20])
        self.grampas_tractor.setText(equip[21])
        self.resortes_tractor.setText(equip[22])
        self.calcos_tractor.setText(equip[23])
        self.kithid.setText(equip[24])
        self.kittran.setText(equip[25])
        self.teflon.setText(equip[26])
        self.precintos.setText(equip[27])

    def load_cosechadora(self, equip):
        self.ID_C.setText(str(equip[0]))
        self.cosechadora_marca.setText(str(equip[1]))
        self.cosechadora_modelo.setText(str(equip[2]))
        self.bases_cosechadora.setText(str(equip[4]))
        self.placaportacade_cosechadora.setText(str(equip[5]))
        self.grampascade_cosechadora.setText(str(equip[6]))
        self.frente_cosechadora.setText(str(equip[7]))
        self.brazos_cosechadora.setText(str(equip[8]))
        self.placaportabr_cosechadora.setText(str(equip[9]))
        self.portarolo_cosechadora.setText(str(equip[10]))
        self.rolo_cosechadora.setText(str(equip[11]))
        self.bulones58_cosechadora.setText(str(equip[12]))
        self.bulones78_cosechadora.setText(str(equip[13]))
        self.bulones20mm_cosechadora.setText(str(equip[14]))
        self.bulones916_cosechadora.setText(str(equip[15]))
        self.bulones12_cosechadora.setText(str(equip[16]))
        self.grampas_cosechadora.setText(str(equip[17]))
        self.resortes_cosechadora.setText(str(equip[18]))
        self.calcos_cosechadora.setText(str(equip[19]))
        
    def load_plataforma(self, equip):
        self.ID_PL.setText(str(equip[0]))
        self.plataforma_marca.setText(str(equip[1]))
        self.plataforma_modelo.setText(str(equip[2]))
        self.bases_pl.setText(str(equip[5]))
        self.brazos_pl.setText(str(equip[6]))
        self.portarolo_pl.setText(str(equip[7]))
        self.rolo_pl.setText(str(equip[8]))
        self.bulones58_pl.setText(str(equip[9]))
        self.bulones12_pl.setText(str(equip[10]))
        self.bulones20mm_pl.setText(str(equip[11]))
        self.bulones916_pl.setText(str(equip[12]))
        self.grampas_pl.setText(str(equip[13]))
        self.resortes_pl.setText(str(equip[14]))
        self.calcos_pl.setText(str(equip[15]))
        self.adaptadores_pl.setText(str(equip[16]))


    #<------------Metodo para borrar todos los line edit------------>
    def delete_all_tractor(self):
        self.ID_T.setText("")
        self.tractor_marca.setText("")
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


    def delete_all_cosechadora(self):
        self.ID_C.setText("")
        self.cosechadora_marca.setText("")
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


    def delete_all_plataforma(self):
        self.ID_PL.setText("")
        self.plataforma_marca.setText("")
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
        self.adaptadores_pl.setText("")

    

    #<------------Metodos para reiniciar todos los line edit------------>
    def reset_all_tractor(self):
        self.ID_T.setText("")
        self.tractor_marca.setText("")
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
        self.mangueras.setText("-")
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

    def reset_all_cosechadora(self):
        self.ID_C.setText("")
        self.cosechadora_marca.setText("")
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
        
    def reset_all_plataforma(self):
        self.ID_PL.setText("")
        self.plataforma_marca.setText("")
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
        self.adaptadores_pl.setText("-")


    def pag_actual(self, select_machine):
            if select_machine == "Tractor":
                self.edit_pages.setCurrentWidget(self.page_tractor)
            elif select_machine == "Cosechadora":
                self.edit_pages.setCurrentWidget(self.page_cosechadora)
            elif select_machine == "Plataforma":
                self.edit_pages.setCurrentWidget(self.page_plataforma)
            else:
                pass



