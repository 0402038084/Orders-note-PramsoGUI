import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5 import uic 
from cls.cls_database import comunication_pramso_database
from cls.cls_convert_to_pdf import pdfclass
from cls.cls_search_ol import buscarorderlist 


 
class imprimiropciones(QDialog):
    def __init__(self):
        super(imprimiropciones, self).__init__()
        uic.loadUi("Interface/printoptions.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog
        self.imprimir.clicked.connect(lambda: self.comprobacion_de_impresion())
        self.cerrar.clicked.connect(lambda: self.close())

        self.database = comunication_pramso_database()

        #<------------Table configuration------------>
        self.cliente_edit.setReadOnly(True)
        self.tractor_edit.setReadOnly(True)
        self.idtedit.setReadOnly(True)
        self.cosechadora_edit.setReadOnly(True)
        self.idcedit.setReadOnly(True)
        self.plataforma_sojera.setReadOnly(True)
        self.idpledit_sojero.setReadOnly(True)
        self.plataforma_maicera.setReadOnly(True)
        self.idpledit_maicero.setReadOnly(True)
        self.observaciones.setReadOnly(False)
        self.fechentrega.setReadOnly(True)


    def cargar_pedido_seleccionado(self, list_pedido):
        d = list_pedido[0]
        f = datetime.datetime.now()
        self.cliente_edit.setText(d[1])
        self.tractor_edit.setText(d[3])
        self.idtedit.setText(d[4])
        self.cosechadora_edit.setText(d[5])
        self.idcedit.setText(d[6])
        self.plataforma_sojera.setText(d[7])
        self.idpledit_sojero.setText(d[8])
        self.plataforma_maicera.setText(d[9])
        self.idpledit_maicero.setText(d[10])
        self.observaciones.setText(d[12])
        self.fechentrega.setText(str(f.date())) 

    def comprobacion_de_impresion(self):
        idt = str(self.idtedit.text().upper())
        combobox_sojero = str(self.sojerokit.currentText())
        combobox_maicero = str(self.maicerokit.currentText())
        combobox_tractor = str(self.kitresortes.currentText())
        idpls = str(self.idpledit_sojero.text().upper())
        idplm = str(self.idpledit_maicero.text().upper())
        Ok = 0
        first_msg = 0
        if idt == "-":
           Ok = 1
        else: 
            if combobox_tractor == "Seleccionar":
                QMessageBox.warning(self, 'Error', 'No se han completado las configuraciones', QMessageBox.Ok)
                first_msg = 1
            else:
                Ok = 1

        if idpls == "-":
            Ok = Ok + 1
        else:
            if combobox_sojero == "Seleccionar":
                if first_msg != 1:
                    QMessageBox.warning(self, 'Error', 'No se han completado las configuraciones', QMessageBox.Ok)
                    first_msg = 1
                else: 
                    pass
            else: 
                Ok = Ok + 1

        if idplm == "-":
            Ok = Ok + 1
        else:
            if combobox_maicero == "Seleccionar":
                if first_msg != 1:
                    QMessageBox.warning(self, 'Error', 'No se han completado las configuraciones', QMessageBox.Ok)
                    first_msg = 1
                else: 
                    pass
            else: 
                Ok = Ok + 1

        if Ok == 3:
            self.centrodeimpresion()
        else: 
            pass
        



    def centrodeimpresion(self):
        idt = str(self.idtedit.text().upper())
        idc = str(self.idcedit.text().upper())
        idpls = str(self.idpledit_sojero.text().upper())
        idplm = str(self.idpledit_maicero.text().upper())
        if idt == "-":
            pass
        elif idt == "":
            pass
        else:
            self.impresion_tractor()

        if idc == "-":
            pass
        elif idc == "":
            pass
        else: 
            self.impresion_cosechadora()
        
        if idpls == "-" and  idplm == "-":
            pass
        else: 
            self.plataforma_impresion()
        
        if idt == "-" and idc == "-" and idpls == "-" and idplm == "-":
            QMessageBox.warning(self, 'Error', 'No hay ningun equipo para imprimir', QMessageBox.Ok)
 

    def impresion_tractor(self):
        
        kit_resortes =  str(self.kitresortes.currentText().upper())

        if kit_resortes == "SIN KIT DE RESORTES":
            f = datetime.datetime.now()
            cliente = str(self.cliente_edit.text().upper())
            fechadeentrega = str(str(f.day)+"/"+str(f.month)+"/"+str(f.year))
            nombretractor = str(self.tractor_edit.text().upper())
            idt = str(self.idtedit.text().upper())
            tractor = self.database.control_entrega_tractor(idt)
            tractor_seleccionado = tractor[0]
            tractor_entrega = [cliente, fechadeentrega, nombretractor, idt]
            for x in range (len(tractor_seleccionado)):
                if x > 4:
                    tractor_entrega.append(tractor_seleccionado[x])

                if x == 24:
                    tractor_entrega.append("-")
            fnamepdf_tractor = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
            pdf = pdfclass()
            pdf.control_entrega_tractor(tractor_entrega, fnamepdf_tractor)
        elif kit_resortes == "KIT DE RESORTES":
            f = datetime.datetime.now()
            cliente = str(self.cliente_edit.text().upper())
            fechadeentrega = str(str(f.day)+"/"+str(f.month)+"/"+str(f.year))
            nombretractor = str(self.tractor_edit.text().upper()) + " + KIT"
            idt = str(self.idtedit.text().upper())
            tractor = self.database.control_entrega_tractor(idt)
            tractor_seleccionado = tractor[0]
            tractor_entrega = [cliente, fechadeentrega, nombretractor, idt]
            for x in range (len(tractor_seleccionado)):
                if x > 4:
                    tractor_entrega.append(tractor_seleccionado[x])

                if x == 24:
                    tractor_entrega.append("2")
            
            fnamepdf_tractor = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
            pdf = pdfclass()
            pdf.control_entrega_tractor(tractor_entrega, fnamepdf_tractor)

    def impresion_cosechadora(self):
        idc = str(self.idcedit.text().upper())
        f = datetime.datetime.now()
        cliente = str(self.cliente_edit.text().upper())
        fechadeentrega = str(str(f.day)+"/"+str(f.month)+"/"+str(f.year))
        nombrecosechadora = str(self.cosechadora_edit.text().upper())
        cosechadora = self.database.control_entrega_cosechadora(idc)
        cosechadora_seleccionada = cosechadora[0]
        cosechadora_entrega = [cliente, fechadeentrega, nombrecosechadora, idc]
        for x in range (len(cosechadora_seleccionada)):
            if x > 4:
                cosechadora_entrega.append(cosechadora_seleccionada[x])

        fnamepdf_cosechadora = QFileDialog()
        x = fnamepdf_cosechadora.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
        pdf = pdfclass()
        pdf.control_entrega_cosechadora(cosechadora_entrega, x)

        

    def plataforma_impresion(self):
        
        idpls = str(self.idpledit_sojero.text().upper())
        sojero = str(self.plataforma_sojera.text().upper())
        maicero = str(self.plataforma_maicera.text().upper())
        idplm = str(self.idpledit_maicero.text().upper())
        combobox_sojero = str(self.sojerokit.currentText())
        combobox_maicero = str(self.maicerokit.currentText())
        f = datetime.datetime.now()
        cliente = str(self.cliente_edit.text().upper())
        fechadeentrega = str(str(f.day)+"/"+str(f.month)+"/"+str(f.year))

        if idpls == "-":
            if idplm  == "-":
                pass
            elif combobox_maicero == "KIT":
                plataforma = self.database.control_entrega_maicero(idplm)
                plataforma_seleccionada = plataforma[0]
                maicero = "Kit maicero " + maicero
                plataforma_seleccionada_maicera = [cliente, fechadeentrega, maicero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        if x == 8:
                            plataforma_seleccionada_maicera.append("-")   
                        elif x == 9:
                            plataforma_seleccionada_maicera.append("-")
                        else:
                            plataforma_seleccionada_maicera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
                pdf = pdfclass()
                pdf.control_entrega_plataforma(plataforma_seleccionada_maicera, fnamepdf_plataforma)
            elif combobox_maicero == "COMPLETO":
                plataforma = self.database.control_entrega_maicero(idplm)
                plataforma_seleccionada = plataforma[0]
                maicero = "Maicero " + maicero
                plataforma_seleccionada_maicera = [cliente, fechadeentrega, maicero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        plataforma_seleccionada_maicera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
                pdf = pdfclass()
                pdf.control_entrega_plataforma(plataforma_seleccionada_maicera, fnamepdf_plataforma)
        elif combobox_sojero == "KIT":
            if idplm == "-":
                plataforma = self.database.control_entrega_sojero(idpls)
                plataforma_seleccionada = plataforma[0]
                sojero = "Kit " + sojero
                plataforma_seleccionada_sojera = [cliente, fechadeentrega, sojero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        if x == 8:
                            plataforma_seleccionada_sojera.append("-")   
                        elif x == 9:
                            plataforma_seleccionada_sojera.append("-")
                        else:
                            plataforma_seleccionada_sojera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
                pdf = pdfclass()
                pdf.control_entrega_plataforma(plataforma_seleccionada_sojera, fnamepdf_plataforma)
            elif combobox_maicero == "KIT":
                plataforma = self.database.control_entrega_sojero(idpls)
                plataforma_seleccionada = plataforma[0]
                sojero = "Kit " + sojero
                plataforma_seleccionada_sojera = [cliente, fechadeentrega, sojero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        if x == 8:
                            plataforma_seleccionada_sojera.append("-")   
                        elif x == 9:
                            plataforma_seleccionada_sojera.append("-")
                        else:
                            plataforma_seleccionada_sojera.append(plataforma_seleccionada[x])
                plataforma = self.database.control_entrega_maicero(idplm)
                plataforma_seleccionada = plataforma[0]
                maicero = "Kit " + maicero
                plataforma_seleccionada_maicera = [cliente, fechadeentrega, maicero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        if x == 8:
                            plataforma_seleccionada_maicera.append("-")   
                        elif x == 9:
                            plataforma_seleccionada_maicera.append("-")
                        else:
                            plataforma_seleccionada_maicera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
                pdf = pdfclass()
                pdf.control_entrega_plataformas(plataforma_seleccionada_sojera, plataforma_seleccionada_maicera, fnamepdf_plataforma)
            elif combobox_maicero == "COMPLETO":
                plataforma = self.database.control_entrega_sojero(idpls)
                plataforma_seleccionada = plataforma[0]
                sojero = "Kit " + sojero
                plataforma_seleccionada_sojera = [cliente, fechadeentrega, sojero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        if x == 8:
                            plataforma_seleccionada_sojera.append("-")   
                        elif x == 9:
                            plataforma_seleccionada_sojera.append("-")
                        else:
                            plataforma_seleccionada_sojera.append(plataforma_seleccionada[x])
                plataforma = self.database.control_entrega_maicero(idplm)
                plataforma_seleccionada = plataforma[0]
                maicero = "Maicero " + maicero
                plataforma_seleccionada_maicera = [cliente, fechadeentrega, maicero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        plataforma_seleccionada_maicera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
                pdf = pdfclass()
                pdf.control_entrega_plataformas(plataforma_seleccionada_maicera, plataforma_seleccionada_sojera, fnamepdf_plataforma)
        elif combobox_sojero == "COMPLETO":
            if idplm == "-":
                plataforma = self.database.control_entrega_sojero(idpls)
                plataforma_seleccionada = plataforma[0]
                sojero = "Sojero "+ sojero
                plataforma_seleccionada_sojera = [cliente, fechadeentrega, sojero, idplm]
                pdf = pdfclass()
                pdf.control_entrega_plataforma(plataforma_seleccionada_sojera, fnamepdf_plataforma)
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        plataforma_seleccionada_sojera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
            elif combobox_maicero == "KIT":
                plataforma = self.database.control_entrega_sojero(idpls)
                plataforma_seleccionada = plataforma[0]
                sojero = "Sojero "+ sojero
                plataforma_seleccionada_sojera = [cliente, fechadeentrega, sojero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        plataforma_seleccionada_sojera.append(plataforma_seleccionada[x])
                plataforma = self.database.control_entrega_maicero(idplm)
                plataforma_seleccionada = plataforma[0]
                maicero = "Kit " + maicero
                plataforma_seleccionada_maicera = [cliente, fechadeentrega, maicero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        if x == 8:
                            plataforma_seleccionada_maicera.append("-")   
                        elif x == 9:
                            plataforma_seleccionada_maicera.append("-")
                        else:
                            plataforma_seleccionada_maicera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')
                pdf = pdfclass()
                pdf.control_entrega_plataformas(plataforma_seleccionada_sojera, plataforma_seleccionada_maicera, fnamepdf_plataforma)
            elif combobox_maicero == "COMPLETO":
                plataforma = self.database.control_entrega_sojero(idpls)
                plataforma_seleccionada = plataforma[0]
                sojero = "Sojero "+ sojero
                plataforma_seleccionada_sojera = [cliente, fechadeentrega, sojero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        plataforma_seleccionada_sojera.append(plataforma_seleccionada[x])
                plataforma = self.database.control_entrega_maicero(idplm)
                plataforma_seleccionada = plataforma[0]
                maicero = "Maicero " + maicero
                plataforma_seleccionada_maicera = [cliente, fechadeentrega, maicero, idplm]
                for x in range (len(plataforma_seleccionada)):
                    if x > 5:
                        plataforma_seleccionada_maicera.append(plataforma_seleccionada[x])
                fnamepdf_plataforma = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'Text files (*.pdf)')       
        else:
            pass

